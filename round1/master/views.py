from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from pytz import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import *
from .models import *
from student.models import Student, TaskSubmissions
from student.serializers import StudentSerializer, TaskSubmissionSerializer


# Create your views here.

def add(a, b):
    return int(a + b)


def sub(a, b):
    return int(a - b)


def mul(a, b):
    return int(a * b)


def divide(a, b):
    return int(a / b)


def home(request):
    return render(request, 'home.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            return render(request, 'master/signin.html', {'messages': {"username": "User not found"}})
        try:
            user_data = authenticate(username=username, password=password)
            login(request, user_data)
        except:
            return render(request, 'master/signin.html', {'messages': {"password": "Wrong password"}})
        if not user.Is_master:
            return render(request, 'master/signin.html', {'messages': {"username": "User not found"}})
        return redirect('/master/dashboard')
    return render(request, 'master/signin.html')


def signup(request):
    if request.method == 'POST':
        user_model = User.objects.all()
        existing_username = [user.username for user in user_model]
        existing_mail = [user.email for user in user_model]
        if request.POST['Username'] in existing_username:
            return render(request, 'master/signup.html', {"messages": {'Username': ['Username already exists']}})
        elif request.POST['Mail'] in existing_mail:
            return render(request, 'master/signup.html', {"messages": {'Mail': ['MailId already exists']}})
        serializer = MasterSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            User.objects.create_user(
                username=serializer.data['Username'],
                email=serializer.data['Mail'],
                password=request.POST['password'],
                Is_master=True
            )
            return redirect('/master/signin')
    return render(request, 'master/signup.html')


@login_required
def dashboard(request):
    master = Master.objects.get(Username=request.user.username)
    student_model = Student.objects.filter(MasterData=master.id)
    student_data = StudentSerializer(student_model, many=True)
    task_sub_model = TaskSubmissions.objects.filter(MasterData=master.id)
    correct_tasks = task_sub_model.filter(Is_correct=True)
    wrong_tasks = task_sub_model.filter(Is_correct=False)
    data = {
        "Students": len(student_model),
        "cor_results": len(correct_tasks),
        "wro_results": len(wrong_tasks),
        "student_data": student_data.data
    }
    return render(request, 'master/dashboard.html', {"data": data})


@login_required
def create_task(request):
    master_model = Master.objects.get(Username=request.user.username)
    student_model = Student.objects.filter(MasterData=master_model.id)
    student_data = StudentSerializer(student_model, many=True)
    if request.method == 'POST':
        data = request.POST.copy()
        lo = int(data['LeftOperand'])
        ro = int(data['RightOperand'])
        if data['Operation'] == 'Addition':
            data['Solution'] = add(lo, ro)
        elif data['Operation'] == 'Subtraction':
            data['Solution'] = sub(lo, ro)
        elif data['Operation'] == 'Multiplication':
            data['Solution'] = mul(lo, ro)
        elif data['Operation'] == 'Division':
            if ro == 0:
                return render(request, 'master/taskcreation.html', {
                    "messages": {"RightOperand": ['Right Operand cannot be zero']}, "students": student_data.data})
            data['Solution'] = divide(lo, ro)
        data['Description'] = "Find the {} fo the given input {} & {}.".format(data['Operation'], lo, ro)
        data['MasterData'] = master_model.id
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/master/dashboard')
        else:
            print(serializer.errors)
            return render(request, 'master/taskcreation.html', {
                "messages": error(serializer.errors), "students": student_data.data})

    return render(request, 'master/taskcreation.html', {"students": student_data.data})


@login_required
def profile(request):
    master_model = Master.objects.get(Username=request.user.username)
    master_data = MasterSerializer(master_model)
    return render(request, 'master/profile.html', {"data": master_data.data})


@login_required
def submitted_tasks(request):
    master_model = Master.objects.get(Username=request.user.username)
    submitted = TaskSubmissions.objects.filter(MasterData=master_model.id).filter(~Q(Is_reviewed=True))
    serializer = TaskSubmissionSerializer(submitted, many=True)
    if request.method == 'POST':
        submission_data = TaskSubmissions.objects.get(id=request.POST['id'])
        solution = submission_data.TaskData.Solution
        submission_data.Is_reviewed = True
        if submission_data.Solution == solution:
            submission_data.Is_correct = True
        else:
            submission_data.Is_correct= False
        submission_data.save()
        return redirect('/master/task/submitted')
    return render(request, 'master/submittedtask.html', {"data": serializer.data})


@login_required
def evaluated_task(request):
    master_model = Master.objects.get(Username=request.user.username)
    submitted = TaskSubmissions.objects.filter(MasterData=master_model.id).filter(Is_reviewed=True)
    serializer = TaskSubmissionSerializer(submitted, many=True)
    return render(request, 'master/evaluatedtask.html', {"data": serializer.data})


@login_required
def signout(request):
    logout(request)
    return redirect('/master/signin')


def error(data):
    error_list = {}
    for i in data:
        err_list = {}
        for j in data.get(i):
            err = {i: str(j)}
            error_list.update(err)
        # error_list.append(err_list)
    return error_list

from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import *
from .models import *
from master.models import Master, Task
from master.serializers import TaskSerializer


# Create your views here.


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            return render(request, 'student/signin.html', {'messages': {"username": "User not found"}})
        try:
            user_data = authenticate(username=username, password=password)
            login(request, user_data)
        except:
            return render(request, 'student/signin.html', {'messages': {"password": "Wrong password"}})
        if user.Is_master:
            return render(request, 'student/signin.html', {'messages': {"username": "User not found"}})
        return redirect('/student/dashboard')
    return render(request, 'student/signin.html')


def signup(request):
    master_model = Master.objects.all()
    master_data_list = []
    for i in master_model:
        master_data = {
            "id": i.id,
            "Name": i.Name
        }
        master_data_list.append(master_data)
    if request.method == 'POST':
        user_model = User.objects.all()
        existing_username = [user.username for user in user_model]
        existing_mail = [user.email for user in user_model]
        if request.POST['Username'] in existing_username:
            return render(request, 'student/signup.html', {"messages": {'Username': ['Username already exists']}})
        elif request.POST['Mail'] in existing_mail:
            return render(request, 'student/signup.html', {"messages": {'Mail': ['MailId already exists']}})
        serializer = StudentSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            User.objects.create_user(
                username=serializer.data['Username'],
                email=serializer.data['Mail'],
                password=request.POST['password'],
                Is_master=False
            )
            return redirect('/student/signin')
    return render(request, 'student/signup.html', {"masters": master_data_list})


@login_required
def dashboard(request):
    student_model = Student.objects.get(Username=request.user.username)
    task = Task.objects.filter(StudentData=student_model.id)
    solved_model = TaskSubmissions.objects.filter(StudentData=student_model.id)
    solved_id = [sol.TaskData.id for sol in solved_model]
    solved = 0
    unsolved = 0
    for i in task:
        if i.id in solved_id:
            solved += 1
        else:
            unsolved += 1
    data = {
        "tasks": len(task),
        "solved": solved,
        "unsolved": unsolved
    }
    return render(request, 'student/dashboard.html', {"data": data})


@login_required
def tasks(request):
    student_model = Student.objects.get(Username=request.user.username)
    task = Task.objects.filter(StudentData=student_model.id)
    solved_model = TaskSubmissions.objects.filter(StudentData=student_model.id)
    solved_id = [sol.TaskData.id for sol in solved_model]
    unsolved = []
    for i in task:
        if i.id not in solved_id:
            unsolved.append(i)
    serializer = TaskSerializer(unsolved, many=True)
    if request.method == 'POST':
        detail = request.POST.copy()
        task_data = task.get(id=detail['id'])
        data = {
            "TaskData": detail['id'],
            "Solution": detail['Solution'],
            "MasterData": task_data.MasterData.id,
            "StudentData": student_model.id,
            "Description": task_data.Description
        }
        submissionserializer = TaskSubmissionSerializer(data=data)
        if submissionserializer.is_valid():
            submissionserializer.save()
            return redirect('/student/tasks')
        else:
            return render(request, 'student/tasks.html', {"data": serializer.data})
    return render(request, 'student/tasks.html', {"data": serializer.data})


@login_required
def solved_tasks(request):
    student_model = Student.objects.get(Username=request.user.username)
    solved_model = TaskSubmissions.objects.filter(StudentData=student_model.id)
    serializer = TaskSubmissionSerializer(solved_model, many=True)
    return render(request, 'student/solved_tasks.html', {"data": serializer.data})


@login_required
def profile(request):
    student_model = Student.objects.get(Username=request.user.username)
    student_data = StudentSerializer(student_model)
    return render(request, 'student/profile.html', {"data": student_data.data})


@login_required
def signout(request):
    logout(request)
    return redirect('/student/signin')


def error(data):
    error_list = {}
    for i in data:
        err_list = {}
        for j in data.get(i):
            err = {i: str(j)}
            error_list.update(err)
        # error_list.append(err_list)
    return error_list

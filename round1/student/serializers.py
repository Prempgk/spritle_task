from rest_framework.serializers import ModelSerializer
from .models import *


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class TaskSubmissionSerializer(ModelSerializer):
    class Meta:
        model = TaskSubmissions
        fields = '__all__'

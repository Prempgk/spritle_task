from rest_framework.serializers import ModelSerializer
from .models import *


class MasterSerializer(ModelSerializer):
    class Meta:
        model = Master
        fields = '__all__'


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.

class Master(models.Model):
    username_validator = UnicodeUsernameValidator
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=150, null=False, blank=False)
    Username = models.CharField(max_length=20, unique=True, null=False, blank=False,
                                validators=[MinLengthValidator(5), UnicodeUsernameValidator])
    Mail = models.EmailField(unique=True, null=False, blank=False)
    MasterIn = models.CharField(max_length=150, null=False, blank=False)
    Address = models.TextField(null=False, blank=False)


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    MasterData = models.ForeignKey(Master, on_delete=models.CASCADE, null=False, blank=False)
    Operation = models.CharField(max_length=100, null=False, blank=False)
    LeftOperand = models.BigIntegerField(null=False, blank=False)
    RightOperand = models.BigIntegerField(null=False, blank=False)
    StudentData = models.ManyToManyField('student.Student', blank=False)
    Description = models.TextField(null=False, blank=False)
    Notes = models.TextField(null=True, blank=True)
    Solution = models.BigIntegerField(null=False, blank=False)


User.add_to_class('Is_master', models.BooleanField(null=False, blank=False, default=False))

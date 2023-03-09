from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from master.models import Master, Task


# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=150, null=False, blank=False)
    Username = models.CharField(max_length=20, unique=True, null=False, blank=False,
                                validators=[MinLengthValidator(5), UnicodeUsernameValidator])
    Mail = models.EmailField(unique=True, null=False, blank=False)
    MasterData = models.ForeignKey(Master, on_delete=models.CASCADE, null=False, blank=False)
    Standard = models.CharField(max_length=50, null=False, blank=False)
    SchoolName = models.TextField(null=False, blank=False)
    Address = models.TextField(null=False, blank=False)
    Age = models.PositiveIntegerField(null=False, blank=False, validators=[MinValueValidator(1)])


class TaskSubmissions(models.Model):
    id = models.AutoField(primary_key=True)
    TaskData = models.ForeignKey(Task, on_delete=models.CASCADE, null=False, blank=False)
    MasterData = models.ForeignKey(Master, on_delete=models.CASCADE, null=False, blank=False)
    Solution = models.PositiveBigIntegerField(null=False, blank=False)
    Description = models.TextField(null=True, blank=True)
    StudentData = models.ForeignKey(Student, on_delete=models.CASCADE, null=False, blank=False)
    Submitted_at = models.DateTimeField(null=False, blank=False, default=timezone.now)
    Is_reviewed = models.BooleanField(null=False, blank=False, default=False)
    Is_correct = models.BooleanField(null=True, blank=True)

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Exam(models.Model):
    course = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
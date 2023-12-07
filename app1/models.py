from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class student_model(User):
    roll_number=models.CharField(max_length=10)
    phone_number=models.PositiveBigIntegerField()
    date_of_birth=models.DateField(auto_now=False,auto_now_add=False)
    stream=models.CharField(max_length=50,choices=[['CSE','CSE'],['ECE','ECE'],['MECH','MECH'],['EEE','EEE'],['CIVIL','CIVIL'],['IT','IT']])
    gender=models.CharField(max_length=10,choices=[['Male','Male'],['Female','Female'],['Others','Others']])
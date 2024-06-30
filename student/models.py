from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class otp_model(models.Model):
    otp_no = models.PositiveIntegerField()
    username = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)


class student_model(User):
    roll_number = models.CharField(max_length=10)
    phone_number = models.PositiveBigIntegerField()
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    stream = models.CharField(
        max_length=50,
        choices=[
            ["CSE", "CSE"],
            ["ECE", "ECE"],
            ["MECH", "MECH"],
            ["EEE", "EEE"],
            ["CIVIL", "CIVIL"],
            ["IT", "IT"],
        ],
    )
    section = models.CharField(
        choices=[["1", "1"], ["2", "2"], ["3", "3"], ["4", "4"]], max_length=10
    )
    gender = models.CharField(
        max_length=10,
        choices=[["Male", "Male"], ["Female", "Female"], ["Others", "Others"]],
    )


class buy_course_model(models.Model):
    oid = models.AutoField(primary_key=True)
    teacher_id = models.PositiveBigIntegerField()
    stud_id = models.PositiveBigIntegerField()
    course_id = models.PositiveBigIntegerField()
    bougth_date = models.DateTimeField(auto_now=True)

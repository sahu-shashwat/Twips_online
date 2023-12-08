from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class teacher_model(User):
    teacher_id=models.PositiveIntegerField()
    phone_number=models.PositiveBigIntegerField()
    year_of_experience=models.PositiveSmallIntegerField()
    gender=models.CharField(max_length=10,choices=[['Male','Male'],['Female','Female'],['Others','Others']])


from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class teacher_model(User):
    tid=models.CharField(max_length=10)
    phone_number=models.PositiveBigIntegerField()
    date_of_birth=models.DateField(auto_now=False,auto_now_add=False)
    yoe=models.PositiveBigIntegerField()
    gender=models.CharField(max_length=10,choices=[['Male','Male'],['Female','Female'],['Others','Others']])
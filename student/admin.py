from django.contrib import admin
from student.models import student_model
# Register your models here.

class student_admin(admin.ModelAdmin):
    list_display=['username','first_name','last_name','email','roll_number','phone_number','date_of_birth','stream','section','gender','password']
admin.site.register(student_model,student_admin)
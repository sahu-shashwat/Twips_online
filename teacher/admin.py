from django.contrib import admin
from teacher.models import teacher_model
# Register your models here.

class teacher_admin(admin.ModelAdmin):
    list_display=['username','first_name','last_name','email','teacher_id','phone_number','year_of_experience','gender','password']
admin.site.register(teacher_model,teacher_admin)    
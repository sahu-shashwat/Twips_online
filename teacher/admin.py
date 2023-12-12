from django.contrib import admin
from teacher.models import teacher_model,course_model,domain_model
# Register your models here.

class teacher_admin(admin.ModelAdmin):
    list_display=['username','first_name','last_name','email','teacher_id','phone_number','year_of_experience','gender','password']
admin.site.register(teacher_model,teacher_admin) 

class domain_admin(admin.ModelAdmin):
    list_display=['did','domain_name','desc']
admin.site.register(domain_model,domain_admin)

class course_admin(admin.ModelAdmin):
    list_display=['cid','course_name','desc','image']
admin.site.register(course_model,course_admin)
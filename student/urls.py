from django.urls import path
from student.views import student_view,otp_view


app_name='student'

urlpatterns = [
    path(route='register/',view=student_view,name='register'),
    path(route='otp/',view=otp_view,name='otp'),
]

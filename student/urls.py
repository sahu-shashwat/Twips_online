from django.urls import path
from student.views import student_view,otp_view,student_login_view,home_view,logout_view,all_course,buy_course

app_name='student'

urlpatterns = [
    path(route='register/',view=student_view,name='register'),
    path(route='otp/',view=otp_view,name='otp'),
    path(route='login/',view=student_login_view,name='login'),
    path(route='home/',view=home_view,name='home'),
    path(route='logout/',view=logout_view,name='logout'),
    path(route='all_course/',view=all_course,name='all_course'),
    path(route='buy_course/<int:pk>',view=buy_course,name='buy_course'),
]

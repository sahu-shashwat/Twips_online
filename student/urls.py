from django.urls import path
from app1.views import student_view,otp_view


app_name='app1'

urlpatterns = [
    path(route='register/',view=student_view,name='register'),
    path(route='otp/',view=otp_view,name='otp'),
]

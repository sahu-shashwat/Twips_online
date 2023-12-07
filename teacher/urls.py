from django.urls import path
from teacher.views import teacher_view,otp_view


app_name='teacher'

urlpatterns = [
    path(route='register/',view=teacher_view,name='register'),
    path(route='otp/',view=otp_view,name='otp'),
]

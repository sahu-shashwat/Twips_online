from django.urls import path
from teacher.views import teacher_view,teacher_otp_view,teacher_login_view,teacher_home_view,teacher_logout_view

app_name='teacher'

urlpatterns = [
    path(route='register/',view=teacher_view,name='register'),
    path(route='otp/',view=teacher_otp_view,name='otp'),
    path(route='login/',view=teacher_login_view,name='login'),
    path(route='home/',view=teacher_home_view,name='home'),
    path(route='logout/',view=teacher_logout_view,name='logout'),
]

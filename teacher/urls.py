from django.urls import path
from teacher.views import teacher_view,teacher_otp_view,teacher_login_view,teacher_home_view,teacher_logout_view,register_course,register_domain,update_course,update_domain,delete_course,delete_domain

app_name='teacher'

urlpatterns = [
    path(route='register/',view=teacher_view,name='register'),
    path(route='otp/',view=teacher_otp_view,name='otp'),
    path(route='login/',view=teacher_login_view,name='login'),
    path(route='home/',view=teacher_home_view,name='home'),
    path(route='logout/',view=teacher_logout_view,name='logout'),
    path(route='register_domain/',view=register_domain,name='register_domain'),
    path(route='register_course/',view=register_course,name='register_course'),
    path(route='update_course/<int:pk>/',view=update_course,name='update_course'),
    path(route='update_domain/<int:pk>/',view=update_domain,name='update_domain'),
    path(route='delete_course/<int:pk>/',view=delete_course,name='delete_course'),
    path(route='delete_domain/<int:pk>/',view=delete_domain,name='delete_domain'),
]

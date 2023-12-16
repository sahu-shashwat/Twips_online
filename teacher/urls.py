from django.urls import path
from teacher.views import (
    teacher_view,
    teacher_otp_view,
    teacher_login_view,
    teacher_home_view,
    teacher_logout_view,
    register_course,
    register_domain,
    update_course,
    update_domain,
    delete_course,
    delete_domain,
    list_course,
    register_video,
    update_video,
    delete_video,
    list_video,
    forgot_pwd_view,
    changepwd_view,
)

app_name = "teacher"

urlpatterns = [
    path(route="register/", view=teacher_view, name="register"),
    path(route="otp/<int:pk>/", view=teacher_otp_view, name="otp"),
    path(route="login/", view=teacher_login_view, name="login"),
    path(route="home/", view=teacher_home_view, name="home"),
    path(route="logout/", view=teacher_logout_view, name="logout"),
    path(route="register_domain/", view=register_domain, name="register_domain"),
    path(route="register_course/", view=register_course, name="register_course"),
    path(route="update_course/<int:pk>/", view=update_course, name="update_course"),
    path(route="update_domain/<int:pk>/", view=update_domain, name="update_domain"),
    path(route="delete_course/<int:pk>/", view=delete_course, name="delete_course"),
    path(route="delete_domain/<int:pk>/", view=delete_domain, name="delete_domain"),
    path(route="list_course/", view=list_course, name="list_course"),
    path(route="register_video/", view=register_video, name="register_video"),
    path(route="update_video/<int:pk>/", view=update_video, name="update_video"),
    path(route="delete_video/<int:pk>/", view=delete_video, name="delete_video"),
    path(route="list_video/<int:pk>/", view=list_video, name="list_video"),
    path(route='forgotpwd/',view=forgot_pwd_view,name='forgotpwd'),
    path(route='changepwd/<int:pk>/',view=changepwd_view,name='changepwd'),
]

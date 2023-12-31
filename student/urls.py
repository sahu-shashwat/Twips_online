from django.urls import path
from student.views import (
    student_view,
    otp_view,
    home_view,
    logout_view,
    all_course,
    buy_course,
    my_course,
    forgot_pwd_view,
    changepwd_view,
    course_video,
)

app_name = "student"

urlpatterns = [
    path(route="register/", view=student_view, name="register"),
    path(route="otp/<int:pk>/", view=otp_view, name="otp"),
    # path(route="login/", view=student_login_view, name="login"),
    path(route="home/", view=home_view, name="home"),
    path(route="logout/", view=logout_view, name="logout"),
    path(route="all_course/", view=all_course, name="all_course"),
    path(route="buy_course/<int:pk>/", view=buy_course, name="buy_course"),
    path(route="my_course/", view=my_course, name="my_course"),
    path(route="course_video/<int:pk>", view=course_video, name="course_video"),
    path(route='forgotpwd/',view=forgot_pwd_view,name='forgotpwd'),
    path(route='changepwd/<int:pk>/',view=changepwd_view,name='changepwd'),
]

from django.shortcuts import render, redirect
from django.http import HttpResponse
from student.models import student_model, buy_course_model
from teacher.models import course_video_model, course_model
from student.forms import student_form, student_login_form
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from django.conf import settings
import random
from django.contrib import messages

# Create your views here.

otp_confirm = None


def student_view(request):
    global otp_confirm
    form = student_form()
    if request.method == "POST":
        form = student_form(request.POST)
        if form.is_valid():
            form.save()

            return redirect("/student/login")
    return render(
        request=request, template_name="student_register.html", context={"form": form}
    )


def otp_view(request):
    if request.method == "POST":
        if str(otp_confirm) == str(request.POST["otp"]):
            return redirect("/student/login")
        else:
            return redirect("/student/register")
    return render(request=request, template_name="st_otp.html")


def student_login_view(request):
    global otp_confirm
    form = student_login_form()
    if request.method == "POST":
        form = student_login_form(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user:
                login(request, user)
                return redirect("/student/home")
            else:
                messages.error(request, "Username or Password is incorrect")
                return redirect("/student/login")
    return render(
        request=request, template_name="student_login.html", context={"form": form}
    )


@login_required(login_url="/student/login")
def home_view(request):
    return render(request=request, template_name="student_home.html")


@login_required(login_url="/student/login")
def logout_view(request):
    logout(request)
    return redirect("/student/login")


def all_course(request):
    res = course_model.objects.all()
    return render(
        request=request, template_name="all_course.html", context={"res": res}
    )


def buy_course(request, pk):
    res = course_model.objects.get(cid=pk)
    if request.method == "POST":
        print(request.user.id, pk)
        buy_course_model.objects.create(stud_id=request.user.id, course_id=pk)
        return HttpResponse("you bougth the course")
    return render(
        request=request, template_name="buy_course.html", context={"res": res}
    )

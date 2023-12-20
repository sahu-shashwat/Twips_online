from django.shortcuts import render, redirect
from django.http import HttpResponse
from student.models import otp_model, buy_course_model
from django.contrib.auth.models import User
from teacher.models import (
    teacher_model,
    domain_model,
    course_model,
    course_video_model,
    chat_model,
)
from teacher.forms import (
    teacher_form,
    teacher_login_form,
    domain_form,
    course_form,
    video_form,
    changepwd_form,
    chat_form,
    tchat_form,
)

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from django.conf import settings
import random
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# Create your views here.

otp_confirm = None


def teacher_view(request):
    form = teacher_form()
    if request.method == "POST":
        form = teacher_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/teacher/login")
    return render(
        request=request, template_name="teacher_register.html", context={"form": form}
    )


def teacher_login_view(request):
    form = teacher_login_form()
    if request.method == "POST":
        form = teacher_login_form(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user:
                if user.is_staff:
                    login(request, user)
                    # messages.success(request, f"welcome to teacher login Mr/Ms {user}")
                    return redirect("/teacher/home")
                else:
                    login(request, user)
                    # messages.success(request, f"welcome to Student login Mr/Ms {user}")
                    return redirect("/student/home")

            else:
                messages.error(request, "username or password is incorrect")
                return redirect("/teacher/login")
    return render(
        request=request, template_name="teacher_login.html", context={"form": form}
    )


@login_required(login_url="/teacher/login")
def teacher_home_view(request):
    res = teacher_model.objects.get(id=request.user.id).payment
    return render(
        request=request, template_name="teacher_home.html", context={"payment": res}
    )


@login_required(login_url="/teacher/login")
def teacher_logout_view(request):
    logout(request)
    return redirect("/teacher/login")


def register_domain(request):
    form = domain_form()
    if request.method == "POST":
        form = domain_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Domain data saved")
        else:
            messages.error(request, "data not saved")
        return redirect("/teacher/list_course")
    return render(
        request=request, template_name="register_domain.html", context={"form": form}
    )


def update_domain(request, pk):
    form = domain_form(instance=domain_model.objects.get(did=pk))
    if request.method == "POST":
        form = domain_form(request.POST, instance=domain_model.objects.get(did=pk))
        if form.is_valid():
            form.save()
            messages.success(request, "domain data updated")
        else:
            messages.error(request, "data not updated")
        return redirect("/teacher/list_course")
    return render(
        request=request, template_name="update_domain.html", context={"form": form}
    )


def register_course(request):
    form = course_form()
    if request.method == "POST" and request.FILES:
        form = course_form(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.tid = request.user.id
            if data:
                form.save()
            messages.success(request, "course data saved")
        else:
            messages.error(request, "data not saved")
        return redirect("/teacher/list_course")
    return render(
        request=request, template_name="register_course.html", context={"form": form}
    )


def update_course(request, pk):
    form = course_form(instance=course_model.objects.get(cid=pk))
    if request.method == "POST" or request.FILES:
        form = course_form(
            request.POST, request.FILES, instance=course_model.objects.get(cid=pk)
        )
        if form:
            form.save()
            messages.success(request, "Course updated")
        else:
            messages.error(request, "data not updated")
        return redirect("/teacher/list_course")
    return render(
        request=request, template_name="update_course.html", context={"form": form}
    )


def delete_course(request, pk):
    res = course_model.objects.get(cid=pk)
    if request.method == "POST":
        res = course_model.objects.get(cid=pk).delete()
        return HttpResponse("deteted")
    return render(
        request=request, template_name="delete_course.html", context={"res": res}
    )


def delete_domain(request, pk):
    res = domain_model.objects.get(did=pk)
    if request.method == "POST":
        res = domain_model.objects.get(did=pk).delete()
        return HttpResponse("deteted")
    return render(
        request=request, template_name="delete_domain.html", context={"res": res}
    )


def list_course(request):
    res = course_model.objects.filter(tid=request.user.id)
    return render(request=request, template_name="list.html", context={"res": res})


def register_video(request):
    form = video_form(course=request.user.id)
    if request.method == "POST":
        form = video_form(request.POST, course=request.user.id)
        if form.is_valid():
            data = form.save(commit=False)
            data.tid = request.user.id
            if data:
                form.save()
            messages.success(request, " video link stored")
        else:
            messages.error(request, " video link not stored")
        return redirect("/teacher/list_course")
    return render(
        request=request, template_name="register_video.html", context={"form": form}
    )


def update_video(request, pk):
    form = video_form(
        instance=course_video_model.objects.get(vid=pk), course=request.user.id
    )
    if request.method == "POST":
        form = video_form(
            request.POST,
            request.FILES,
            instance=course_video_model.objects.get(vid=pk),
            course=request.user.id,
        )
        if form:
            form.save()
            messages.success(request, "video updated")
        else:
            messages.error(request, "video not updated")
        return redirect("/teacher/list_course")
    return render(
        request=request, template_name="update_video.html", context={"form": form}
    )


def delete_video(request, pk):
    res = course_video_model.objects.get(vid=pk)
    if request.method == "POST":
        res = course_video_model.objects.get(vid=pk).delete()
        return HttpResponse("deteted")
    return render(
        request=request, template_name="delete_video.html", context={"res": res}
    )


def list_video(request, pk):
    res = course_video_model.objects.filter(cid=pk)
    return render(
        request=request, template_name="list_video.html", context={"res": res}
    )


def forgot_pwd_view(request):
    res = User.objects.all().values_list("email")
    if request.method == "POST":
        otp = random.randint(000000, 999999)
        email = request.POST["email"]
        otp_model.objects.filter(username=email).delete()
        otp_model.objects.create(otp_no=otp, username=email)
        if (email,) in res:
            subject = "Teacher Verification Code"
            msg = f"""Dear User,
                    Please enter this OTP {otp}.
                    Thankyou..."""
            send_mail(
                subject=subject,
                message=msg,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
            )
            email_id = User.objects.get(email=email)
            return redirect(f"/teacher/otp/{email_id.id}/{email}/")
        else:
            messages.error(request, "Email or OTP is incorrect.")
    return render(request=request, template_name="te_forgotten_pwd.html")


def teacher_otp_view(request, pk, email):
    print(pk, email)
    if request.method == "POST":
        otp_confirm = otp_model.objects.get(username=email)
        if str(otp_confirm.otp_no) == str(request.POST["otp"]):
            otp_model.objects.get(username=email).delete()
            return redirect(f"/teacher/changepwd/{pk}/")
        else:
            return redirect("/teacher/forgotpwd")
    return render(request=request, template_name="teacher_otp.html")


def changepwd_view(request, pk):
    form = changepwd_form()
    if request.method == "POST":
        res = User.objects.get(id=pk)
        form = changepwd_form(request.POST)
        if form.is_valid():
            if (
                form.cleaned_data["enter_new_password"]
                == form.cleaned_data["re_enter_password"]
            ):
                User.objects.filter(id=pk).update(
                    password=make_password(form.cleaned_data["enter_new_password"])
                )
                return redirect("/teacher/login/")
    return render(
        request=request, template_name="createpwd.html", context={"form": form}
    )


def chat_view(request, tid, cid):
    chat = chat_model.objects.filter(tid=tid, sid=request.user.id).order_by("date")
    print(chat)
    print(tid, cid)
    form = chat_form()
    if request.method == "POST" or request.FILES:
        print("haii")
        form = chat_form(request.POST,request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.sid = request.user.id
            data.tid = tid
            data.course_id = cid
            if data:
                form.save()
                return redirect(f"/teacher/chatbox/{tid}/{cid}/")
    return render(
        request=request,
        template_name="chatbox.html",
        context={"form": form, "chat": chat},
    )


def teacher_chat_view(request):
    res = buy_course_model.objects.filter(teacher_id=request.user.id)
    student = User.objects.filter(id__in=res, is_staff=False)
    return render(
        request, template_name="teacher_chat.html", context={"student": student}
    )


def tchat_view(request, sid):
    chat = chat_model.objects.filter(tid=request.user.id, sid=sid).order_by("date")
    print(chat)
    print(sid)
    form = tchat_form()
    if request.method == "POST" or request.FILES:
        form = tchat_form(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.sid = sid
            data.tid = request.user.id
            data.course_id = 0
            if data:
                form.save()
                return redirect(f"/teacher/tchatbox/{sid}/")
    return render(
        request=request,
        template_name="tchatbox.html",
        context={"form": form, "chat": chat},
    )

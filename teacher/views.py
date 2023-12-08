from django.shortcuts import render,redirect
from django.http import HttpResponse
from teacher.models import teacher_model
from teacher.forms import teacher_form,teacher_login_form
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.core.mail import send_mail
from django.conf import settings
import random

# Create your views here.

otp_confirm=None

def teacher_view(request):
    global otp_confirm
    form=teacher_form()
    if request.method=='POST':
        form=teacher_form(request.POST)
        if form.is_valid():
            form.save()
            otp=random.randint(000000,999999)
            otp_confirm=otp
            email=form.cleaned_data['email']
            subject='Teacher Verification Code'
            msg=f'''Dear User,
                    Please enter this OTP {otp}.
                    Thankyou...'''
            send_mail(subject=subject,message=msg,from_email=settings.EMAIL_HOST_USER,recipient_list=[email,])
            return redirect('/teacher/otp')
    return render(request=request,template_name='teacher_register.html',context={'form':form})



def teacher_otp_view(request):
    if request.method=='POST':
        if str(otp_confirm)==str(request.POST['otp']):
            return redirect('/teacher/login')
        else:
            return redirect('/teacher/register')
    return render(request=request,template_name='teacher_otp.html')


def teacher_login_view(request):
    global otp_confirm
    form=teacher_login_form()
    if request.method=='POST':
        form=teacher_login_form(request.POST)
        if form.is_valid():
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user:
                login(request,user)
                return redirect("/teacher/home")
    return render(request=request,template_name='teacher_login.html',context={'form':form})


@login_required(login_url='/teacher/login')
def teacher_home_view(request):
    return render(request=request,template_name='teacher_home.html')

@login_required(login_url='/teacher/login')
def teacher_logout_view(request):
    logout(request)
    return redirect('/teacher/login')
from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import student_model
from app1.forms import student_form
from django.core.mail import send_mail
from django.conf import settings
import random

# Create your views here.


otp_confirm=None

def student_view(request):
    global otp_confirm
    form=student_form()
    if request.method=='POST':
        form=student_form(request.POST)
        if form.is_valid():
            form.save()
            otp=random.randint(000000,999999)
            otp_confirm=otp
            email=form.cleaned_data['email']
            subject='Student Verification Code'
            msg=f'''Dear Student,
                    Please enter this OTP {otp}.
                    Thankyou...'''
            send_mail(subject=subject,message=msg,from_email=settings.EMAIL_HOST_USER,recipient_list=[email,])
            return redirect('/otp')
    return render(request=request,template_name='student_register.html',context={'form':form})



def otp_view(request):
    if request.method=='POST':
        if str(otp_confirm)==str(request.POST['otp']):
            return HttpResponse('Data is Stored')
        else:
            return redirect('/register')
    return render(request=request,template_name='st_otp.html')
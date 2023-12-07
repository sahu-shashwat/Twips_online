from django.shortcuts import render,redirect
from django.http import HttpResponse
from teacher.models import teacher_model
from teacher.forms import teacher_form
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
            subject='teacher Verification Code'
            msg=f'''Dear Sir,
                    Please enter this OTP {otp}.
                    Thankyou...'''
            send_mail(subject=subject,message=msg,from_email=settings.EMAIL_HOST_USER,recipient_list=[email,])
            return redirect('/otp')
    return render(request=request,template_name='teacher_register.html',context={'form':form})



def otp_view(request):
    if request.method=='POST':
        if str(otp_confirm)==str(request.POST['otp']):
            return HttpResponse('Data is Stored')
        else:
            return redirect('/register')
    return render(request=request,template_name='th_otp.html')
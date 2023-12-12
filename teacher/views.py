from django.shortcuts import render,redirect
from django.http import HttpResponse
from teacher.models import teacher_model,domain_model,course_model
from teacher.forms import teacher_form,teacher_login_form,domain_form,course_form
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.core.mail import send_mail
from django.conf import settings
import random
from django.contrib import messages

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
            else:                
                messages.error(request,"username or password is incorrect")
                return redirect("/teacher/login")
    return render(request=request,template_name='teacher_login.html',context={'form':form})


@login_required(login_url='/teacher/login')
def teacher_home_view(request):
    return render(request=request,template_name='teacher_home.html')

@login_required(login_url='/teacher/login')
def teacher_logout_view(request):
    logout(request)
    return redirect('/teacher/login')

def register_domain(request):
    form=domain_form()
    if request.method=='POST':
        form=domain_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Domain data saved")
        else:
            return HttpResponse('data not saved')
    return render(request=request, template_name="register_domain.html", context={"form": form})

def update_domain(request,pk):
    form=domain_form(instance=domain_model.objects.get(did=pk))
    if request.method=='POST':
        form=domain_form(request.POST,instance=domain_model.objects.get(did=pk))
        if form.is_valid():
            form.save()
            return HttpResponse('data updated')
        else:
            return HttpResponse("data not updated")
    return render(request=request,template_name='update_domain.html',context={'form':form})

def register_course(request):
    form=course_form()
    if request.method=='POST' and request.FILES:
        form=course_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("course data saved")
        else:
            return HttpResponse('data not saved')
    return render(request=request, template_name="register_course.html", context={"form": form})

def update_course(request,pk):
    form=course_form(instance=course_model.objects.get(cid=pk))
    if request.method=='POST' and request.FILES:
        form=course_form(request.POST,request.FILES,instance=course_model.objects.get(cid=pk))
        if form.is_valid():
            form.save()
            return HttpResponse('course updated')
        else:
            return HttpResponse("data not updated")
    return render(request=request,template_name='update_course.html',context={'form':form})

def delete_course(request,pk):
    res=course_model.objects.get(cid=pk)
    if request.method=='POST' :
        res=course_model.objects.get(cid=pk).delete()
        return HttpResponse("deteted")
    return render(request=request,template_name='delete_course.html',context={'res':res})

def delete_domain(request,pk):
    res=domain_model.objects.get(did=pk)
    if request.method=='POST':
        res=domain_model.objects.get(did=pk).delete()
        return HttpResponse("deteted")
    return render(request=request,template_name='delete_domain.html',context={'res':res})
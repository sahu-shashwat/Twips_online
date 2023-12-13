from django.shortcuts import render, redirect
from django.http import HttpResponse

def main_home_view(request):
    return render(request=request,template_name='mainhome.html')

from django import forms
from teacher.models import teacher_model,domain_model,course_model
from django.contrib.auth.hashers import make_password
import re
from django.contrib.auth.models import User

class teacher_form(forms.ModelForm):
    confirm_password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=teacher_model
        fields=['username','first_name','last_name','email','teacher_id','phone_number','year_of_experience','gender','password']


    def clean_username(self):
        username=self.cleaned_data['username']
        if not(username[0].isupper()):
            raise forms.ValidationError('Username should starts with uppercase.')
        if len(username)<3:
            raise forms.ValidationError('Username should greater than 3 charecters.')
        if len(username)>15:
            raise forms.ValidationError('Username should less than 3 charecters.')
        return username
    
    def clean_phone(self):
        phone=self.cleaned_data['phone_number']
        if len(str(phone)) != 10:
            raise forms.ValidationError('Phone number should contins 10 numbers only.')
        if str(phone)[0] not in '6789':
            raise forms.ValidationError('Phone number should starts with 6,7,8,9')
        return phone
    
    
    def clean_password(self):
        pwd=self.cleaned_data['password']
        if not(pwd[0].isupper()):
            raise forms.ValidationError('Password should starts with uppercase')
        if len(pwd)<5:
            raise forms.ValidationError('Password should greater than 5 charecters')
        if len(pwd)>15:
            raise forms.ValidationError('Password should less than 15 charecters')
        if len(re.findall('[0-9]',pwd))==0:
            raise forms.ValidationError('Password should contains atleast one number')
        if len(re.findall('[a-z]',pwd))==0:
            raise forms.ValidationError('Password should contains atleast one lowercase')
        if len(re.findall('[^a-z A-z 0-9]',pwd))==0:
            raise forms.ValidationError('Password should contains atleast one special charecter')
        return pwd
    

    def clean_confirm_password(self):
        pwd=self.cleaned_data['confirm_password']
        if not(pwd[0].isupper()):
            raise forms.ValidationError('Confirm password should starts with uppercase')
        if len(pwd)<5:
            raise forms.ValidationError('Confirm password should greater than 5 charecters')
        if len(pwd)>15:
            raise forms.ValidationError('Confirm password should less than 15 charecters')
        if len(re.findall('[0-9]',pwd))==0:
            raise forms.ValidationError('Confirm password should contains atleast one number')
        if len(re.findall('[a-z]',pwd))==0:
            raise forms.ValidationError('Confirm password should contains atleast one lowercase')
        if len(re.findall('[^a-z A-z 0-9]',pwd))==0:
            raise forms.ValidationError('Confirm password should contains atleast one special charecter')
        if self.cleaned_data['password']!=pwd:
            raise forms.ValidationError('Confirm password should be same as password')
        return pwd
    

    def save(self,commit=True):
        user=super().save(commit=False)
        if self.cleaned_data['password']==self.cleaned_data['confirm_password']:
            user.password=make_password(self.cleaned_data['password'])
            if commit:
                user.save()                
            return user

class teacher_login_form(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        temp=User.objects.all().values_list('username')
       
        res=self.cleaned_data['username']
        if(res,) not in temp:
            raise forms.ValidationError('User not found')

    def clean_username(self):
        username=self.cleaned_data['username']
        if not(username[0].isupper()):
            raise forms.ValidationError('Username should starts with uppercase')
        if len(username)<5:
            raise forms.ValidationError('Username should greater than 5 charecters')
        if len(username)>15:
            raise forms.ValidationError('Username should less than 15 charecters')
        return username
    

    def clean_password(self):
        pwd=self.cleaned_data['password']
        if not(pwd[0].isupper()):
            raise forms.ValidationError('Password should starts with uppercase')
        if len(pwd)<5:
            raise forms.ValidationError('Password should greater than 5 charecters')
        if len(pwd)>15:
            raise forms.ValidationError('Password should less than 15 charecters')
        if len(re.findall('[0-9]',pwd))==0:
            raise forms.ValidationError('Password should contains atleast one number')
        if len(re.findall('[a-z]',pwd))==0:
            raise forms.ValidationError('Password should contains atleast one lowercase')
        if len(re.findall('[^a-z A-z 0-9]',pwd))==0:
            raise forms.ValidationError('Password should contains atleast one special charecter')
        return pwd
    
class domain_form(forms.ModelForm):
       class Meta:
        model = domain_model
        fields = "__all__"
     
class course_form(forms.ModelForm):
      class Meta:
        model = course_model
        fields = "__all__"
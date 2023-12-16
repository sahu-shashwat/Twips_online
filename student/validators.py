from django import forms
import re

def clean_enter_new_password(newpwd):
        if not(newpwd[0].isupper()):
            raise forms.ValidationError('Password should starts with uppercase')
        if len(newpwd)<5:
            raise forms.ValidationError('Password should greater than 5 charecters')
        if len(newpwd)>15:
            raise forms.ValidationError('Password should less than 15 charecters')
        if len(re.findall('[0-9]',newpwd))==0:
            raise forms.ValidationError('Password should contains atleast one number')
        if len(re.findall('[a-z]',newpwd))==0:
            raise forms.ValidationError('Password should contains atleast one lowercase')
        if len(re.findall('[^a-z A-z 0-9]',newpwd))==0:
            raise forms.ValidationError('Password should contains atleast one special charecter')
        return newpwd
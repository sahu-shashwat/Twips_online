from django import forms
from student.models import student_model
from django.contrib.auth.hashers import make_password
import re
from django.contrib.auth.models import User
from student.validators import clean_enter_new_password


class student_form(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = student_model
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "roll_number",
            "phone_number",
            "date_of_birth",
            "stream",
            "section",
            "gender",
            "password",
        ]

    def clean_username(self):
        username = self.cleaned_data["username"]
        if not (username[0].isupper()):
            raise forms.ValidationError("Username should starts with uppercase.")
        if len(username) < 3:
            raise forms.ValidationError("Username should greater than 3 charecters.")
        if len(username) > 15:
            raise forms.ValidationError("Username should less than 3 charecters.")
        return username

    def clean_roll(self):
        roll = self.cleaned_data["roll_number"]
        if len(roll) != 10:
            raise forms.ValidationError("Roll number should contains 10 charecters.")
        return roll

    def clean_phone(self):
        phone = self.cleaned_data["phone_number"]
        if len(str(phone)) != 10:
            raise forms.ValidationError("Phone number should contins 10 numbers only.")
        if str(phone)[0] not in "6789":
            raise forms.ValidationError("Phone number should starts with 6,7,8,9")
        return phone

    def clean_password(self):
        pwd = self.cleaned_data["password"]
        if not (pwd[0].isupper()):
            raise forms.ValidationError("Password should starts with uppercase")
        if len(pwd) < 5:
            raise forms.ValidationError("Password should greater than 5 charecters")
        if len(pwd) > 15:
            raise forms.ValidationError("Password should less than 15 charecters")
        if len(re.findall("[0-9]", pwd)) == 0:
            raise forms.ValidationError("Password should contains atleast one number")
        if len(re.findall("[a-z]", pwd)) == 0:
            raise forms.ValidationError(
                "Password should contains atleast one lowercase"
            )
        if len(re.findall("[^a-z A-z 0-9]", pwd)) == 0:
            raise forms.ValidationError(
                "Password should contains atleast one special charecter"
            )
        return pwd

    def clean_confirm_password(self):
        pwd = self.cleaned_data["confirm_password"]
        if not (pwd[0].isupper()):
            raise forms.ValidationError("Confirm password should starts with uppercase")
        if len(pwd) < 5:
            raise forms.ValidationError(
                "Confirm password should greater than 5 charecters"
            )
        if len(pwd) > 15:
            raise forms.ValidationError(
                "Confirm password should less than 15 charecters"
            )
        if len(re.findall("[0-9]", pwd)) == 0:
            raise forms.ValidationError(
                "Confirm password should contains atleast one number"
            )
        if len(re.findall("[a-z]", pwd)) == 0:
            raise forms.ValidationError(
                "Confirm password should contains atleast one lowercase"
            )
        if len(re.findall("[^a-z A-z 0-9]", pwd)) == 0:
            raise forms.ValidationError(
                "Confirm password should contains atleast one special charecter"
            )
        if self.cleaned_data["password"] != pwd:
            raise forms.ValidationError("Confirm password should be same as password")
        return pwd

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data["password"] == self.cleaned_data["confirm_password"]:
            user.password = make_password(self.cleaned_data["password"])
            if commit:
                user.save()
            return user


class student_login_form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data["username"]
        if not (username[0].isupper()):
            raise forms.ValidationError("Username should starts with uppercase")
        if len(username) < 3:
            raise forms.ValidationError("Username should greater than 3 charecters")
        if len(username) > 15:
            raise forms.ValidationError("Username should less than 15 charecters")
        return username

    def clean_password(self):
        pwd = self.cleaned_data["password"]
        if not (pwd[0].isupper()):
            raise forms.ValidationError("Password should starts with uppercase")
        if len(pwd) < 5:
            raise forms.ValidationError("Password should greater than 5 charecters")
        if len(pwd) > 15:
            raise forms.ValidationError("Password should less than 15 charecters")
        if len(re.findall("[0-9]", pwd)) == 0:
            raise forms.ValidationError("Password should contains atleast one number")
        if len(re.findall("[a-z]", pwd)) == 0:
            raise forms.ValidationError(
                "Password should contains atleast one lowercase"
            )
        if len(re.findall("[^a-z A-z 0-9]", pwd)) == 0:
            raise forms.ValidationError(
                "Password should contains atleast one special charecter"
            )
        return pwd

    def clean(self):
        # print(self.__dict__)
        temp = User.objects.all().values_list("username")
        # print(temp)
        res = self.cleaned_data["username"]
        if (res,) not in temp:
            raise forms.ValidationError("User not found")
        

class changepwd_form(forms.Form):
    enter_new_password=forms.CharField(widget=forms.PasswordInput,validators=[clean_enter_new_password,])
    re_enter_password=forms.CharField(widget=forms.PasswordInput)

    def clean_re_enter_password(self):
        paswd=self.cleaned_data['re_enter_password']
        if not(paswd[0].isupper()):
            raise forms.ValidationError('Re enter password should starts with uppercase')
        if len(paswd)<5:
            raise forms.ValidationError('Re enter password should greater than 5 charecters')
        if len(paswd)>15:
            raise forms.ValidationError('Re enter password should less than 15 charecters')
        if len(re.findall('[0-9]',paswd))==0:
            raise forms.ValidationError('Re enter password should contains atleast one number')
        if len(re.findall('[a-z]',paswd))==0:
            raise forms.ValidationError('Re enter password should contains atleast one lowercase')
        if len(re.findall('[^a-z A-z 0-9]',paswd))==0:
            raise forms.ValidationError('Re enter password should contains atleast one special charecter')
        if self.cleaned_data['enter_new_password']!=paswd:
            raise forms.ValidationError('New password and re-entered password should be same as password')
        return paswd

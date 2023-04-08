from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from .models import Student
from django.utils.translation import ugettext_lazy as _
from django.forms.widgets import PasswordInput, TextInput
from django.core.exceptions import ValidationError
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','email','password1', 'password2')

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username','class' : 'reg_form_input_1'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password','class' : 'reg_form_input_1'}))


class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ('reg_no','department', 'batch','mobile_no','address')

class EditProfileForm(forms.ModelForm):
    def reg_no(self):
        reg_no = self.cleaned_data['reg_no']
        if Student.objects.filter(reg_no=reg_no).exists():
            raise ValidationError("register number already exists")
        return reg_no
    class Meta:
        model = Student
        fields = ('reg_no','department', 'batch','mobile_no','address')

   






   
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import StudentProfile
from django.contrib.auth.models import User


class AddNewUser(UserCreationForm):
    email = forms.EmailField(label='ايميل المستخدم',max_length=254,widget=forms.EmailInput(attrs={'class': 'form-control input-solid','required':'required'}))
    password1 = forms.CharField(label='الباسورد',max_length=250,widget=forms.PasswordInput(attrs={'class': 'form-control input-solid','required':'required'}))
    password2 = forms.CharField(label='تاكيد الباسورد',max_length=250,widget=forms.PasswordInput(attrs={'class': 'form-control input-solid','required':'required'}))
    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control input-solid','required':'required'}),
        }
        labels = {
            'username':'اسم المستخدم',
        }



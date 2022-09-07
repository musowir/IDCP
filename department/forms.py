from django import forms
from department.models import DepProfileInfo
from django.contrib.auth.models import User
class DepForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class DepProfileInfoForm(forms.ModelForm):
     class Meta():
         model = DepProfileInfo
         fields = ('department_name', 'bio','phone', 'website')
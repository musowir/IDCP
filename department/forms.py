from dataclasses import field
from django import forms
from department.models import DepProfileInfo, CourseInfo
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

class CourseAddForm(forms.ModelForm):
    class Meta():
        model = CourseInfo
        fields = ('couse_code', 'couse_name', 'department', 'start_date', 'slot','hours_per_week', 'no_of_seats', 'syllabus')
from django import forms
from student.models import StudentInfo
from django.contrib.auth.models import User
class StudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password',)
class StudentProfileInfoForm(forms.ModelForm):
     class Meta():
         model = StudentInfo
         fields = ('exam_reg_no','phone','department','course','cgpa')

from django import forms
from department.models import DepProfileInfo, CourseInfo, Faculty, Notification, Teaches
from django.contrib.auth.models import User
from bootstrap_datepicker_plus.widgets import DatePickerInput

class DepForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class DepProfileInfoForm(forms.ModelForm):
     class Meta():
         model = DepProfileInfo
         fields = ('department_name', 'bio','phone', 'website')

class DateInput(forms.DateInput):
    input_type = 'date'

class CourseAddForm(forms.ModelForm):
    class Meta():
        model = CourseInfo
        fields = ['course_code', 'course_name', 'start_date', 'slot','hours_per_week', 'no_of_seats', 'syllabus']
        widgets={
            'start_date': DatePickerInput(),
        }
        

class NotForm(forms.ModelForm):
    class Meta():
        model= Notification
        fields =('notification',)

class FacForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class FacultyForm(forms.ModelForm):
    class Meta():
        model = Faculty
        fields=('name', 'department', 'isCC')

class TeachesForm(forms.ModelForm):
    class Meta():
        model = Teaches
        fields=('faculty','course')
                
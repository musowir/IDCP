from django.contrib import admin

from student.models import Enroll, StudentInfo

# Register your models here.
admin.site.register(StudentInfo)
admin.site.register(Enroll)
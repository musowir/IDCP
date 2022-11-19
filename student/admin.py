from django.contrib import admin

from student.models import Enroll, StudentInfo, Attendance

# Register your models here.
admin.site.register(StudentInfo)
admin.site.register(Enroll)
admin.site.register(Attendance)
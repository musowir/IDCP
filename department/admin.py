from django.contrib import admin


from department.models import DepProfileInfo, CourseInfo
# Register your models here.
admin.site.register(DepProfileInfo)
admin.site.register(CourseInfo)
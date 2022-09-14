from django.contrib import admin


from department.models import DepProfileInfo, CourseInfo, Notification
# Register your models here.
admin.site.register(DepProfileInfo)
admin.site.register(CourseInfo)
admin.site.register(Notification)
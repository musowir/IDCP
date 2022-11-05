from django.contrib import admin


from department.models import DepProfileInfo, CourseInfo, Faculty, Notification, Teaches
# Register your models here.
admin.site.register(DepProfileInfo)
admin.site.register(CourseInfo)
admin.site.register(Notification)
admin.site.register(Faculty)
admin.site.register(Teaches)



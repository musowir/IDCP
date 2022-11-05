from django.urls import re_path as url
from student import views
# SET THE NAMESPACE!
app_name = 'student'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url('register/',views.register,name='register'),
    url('student_login/',views.student_login,name='student_login'),
    url('stu/', views.index, name='stu'),
    url(r'^enroll/(?P<course_id>\d+)$', views.enrollStudent, name='enroll_student'),
]
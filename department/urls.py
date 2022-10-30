from django.urls import re_path as url
from department import views
# SET THE NAMESPACE!
app_name = 'department'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[

    url('register/',views.register,name='register'),
    url('user_login/',views.user_login,name='user_login'),
    url('course_add/', views.courseAdd, name='course_add'),
    url('notsadd/', views.Notification),
    url(r'^approve/(?P<student_id>\d+)$', views.approve_student, name='approve'),
    url(r'^reject/(?P<student_id>\d+)$', views.reject_student, name='reject'),
    url(r'^delete/(?P<course_id>\d+)$', views.courseDel, name='delete'),
    url(r'^not_delete/(?P<not_id>\d+)$', views.notDel, name='not_delete'),

]
from django.urls import re_path as url
from department import views
# SET THE NAMESPACE!
app_name = 'department'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url('register/',views.register,name='register'),
    url('user_login/',views.user_login,name='user_login'),
    url('dep/', views.index, name='dep')
]
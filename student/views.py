from django.shortcuts import render
from student.forms import StudentForm, StudentProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from student.models import StudentInfo
def index(request):
    return render(request,'student/index.html')
    
@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('welcome'))
def register(request):
    registered = False
    if request.method == 'POST':
        s_user_form = StudentForm(data=request.POST)
        s_profile_form = StudentProfileInfoForm(data=request.POST)
        if s_user_form.is_valid() and s_profile_form.is_valid():
            user = s_user_form.save()
            user.set_password(user.password)
            user.save()
            s_profile = s_profile_form.save(commit=False)
            s_profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                s_profile.profile_pic = request.FILES['profile_pic']
            s_profile.save()
            registered = True
        else:
            print(s_user_form.errors,s_profile_form.errors)
    else:
        s_user_form = StudentForm()
        s_profile_form = StudentProfileInfoForm()
    return render(request,'student/registration.html',
                          {'s_user_form':s_user_form,
                           's_profile_form':s_profile_form,
                           'registered':registered})
def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('s_index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'student/login.html', {})

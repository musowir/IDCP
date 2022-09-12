from django.shortcuts import render,get_object_or_404
import department
from department.forms import DepForm,DepProfileInfoForm, CourseAddForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from department.models import CourseInfo, DepProfileInfo

#@login_required(login_url='/')
def index(request):
    if request.user.is_authenticated:
        depinf = DepProfileInfo.objects.get(user=request.user)
        cour = CourseInfo.objects.filter(department=depinf)
        return render(request,'department/index.html', {'depinf':depinf, 'cour': cour})


def welcome(request):
    deps=DepProfileInfo.objects.all()
    r=[]
    for d in deps:
        c = CourseInfo.objects.filter(department=d.id)
        r.append({'dep':d, 'cor':c})
    return render(request,'department/welcome.html', context={'r':r })
    
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
        user_form = DepForm(data=request.POST)
        profile_form = DepProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.is_staff=True
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = DepForm()
        profile_form = DepProfileInfoForm()
    return render(request,'department/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active and user.is_staff:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive or not a department.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'department/login.html', {})

def courseAdd(request):
    registered = False
    if request.method == 'POST':
        course_form = CourseAddForm(data=request.POST)
        if course_form.is_valid():
            
            course = course_form.save(commit=False)
            
            course.save()
            registered = True
        else:
            print(course_form.errors)
    else:
        course_form = CourseAddForm()
    return render(request,'department/courseadd.html',
                          {
                           'course_form':course_form,
                           'registered':registered})

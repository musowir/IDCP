from asyncio.windows_events import NULL

from django.shortcuts import render
from student.forms import StudentForm, StudentProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from department.models import DepProfileInfo, CourseInfo, Notification
from student.models import Enroll, StudentInfo
from django.contrib import messages
def index(request):
    student = StudentInfo.objects.get(user=request.user)
    deps=DepProfileInfo.objects.all()
    try:
        en = Enroll.objects.get(student=student)
    except Enroll.DoesNotExist:
        en = 0
        
    cor = CourseInfo.objects.filter()
    r=[]
    for d in deps:
        c = CourseInfo.objects.filter(department=d.id)
        r.append({'dep':d, 'cor':c})
    
    if(en != 0):
        notsin = Notification.objects.filter(department= en.course.department)
    else:
        notsin = {}
    
    
    return render(request,'student/index.html', context={'r':r, 'student': student, 'cor':cor, 'en':en, 'notsin':notsin})

def enrollStudent(request, course_id):
    stu = StudentInfo.objects.get(user=request.user)
    cor = CourseInfo.objects.get(id=course_id)    
    en = Enroll(student = stu, course = cor)
    en.save()
    cor.seats_left-=1
    cor.save()
    return HttpResponseRedirect(reverse('s_index'))

    
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
            if user.is_active and not user.is_staff:
                login(request,user)
                return HttpResponseRedirect(reverse('s_index'))
            else:
                messages.success(request, "You are not a student!")
                return HttpResponseRedirect(reverse('welcome'))
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            messages.success(request, "Invalid login details given")
            return HttpResponseRedirect(reverse('welcome'))
    else:
        return render(request, 'student/login.html', {})

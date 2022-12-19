

from django.shortcuts import render
from student.forms import StudentForm, StudentProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from department.models import DepProfileInfo, CourseInfo, Notification
from student.models import Enroll, StudentInfo
from django.contrib import messages
from django.contrib.auth.models import User

def index(request):
    student = StudentInfo.objects.get(user=request.user)
    studey_dep = DepProfileInfo.objects.get(id=student.department.id)
    deps=DepProfileInfo.objects.all()
    try:
        en = Enroll.objects.get(student=student)
    except Enroll.DoesNotExist:
        en = 0
    cor=[]
    corse = CourseInfo.objects.filter()
    for c in corse:
        print(studey_dep.id, c.department.id)
        if c.department.id != studey_dep.id:
            cor.append(c)
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

def requestRemoval(request, enrol_id):
    if enrol_id:
        en = Enroll.objects.get(id=enrol_id)
        en.request_removal = True
        en.save()
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
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
            st = User(username=username, first_name=first_name, last_name=last_name, email=email, is_staff=0)
            st.set_password(password)
            st.save()

            phone = request.POST.get('phone')
            dep_id = request.POST.get('department')
            department = DepProfileInfo.objects.get(id=dep_id)
            course = request.POST.get('course')
            st_inf = StudentInfo(phone=phone, department=department, course=course, user_id=st.id, approved=0)
            st_inf.save()
            messages.success(request, "Regitration Success!")
            return HttpResponseRedirect(reverse('welcome'))
        else:
            messages.warning(request, "Username or email already exist!")
            return HttpResponseRedirect(reverse('welcome'))


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
                messages.warning(request, "You are not a student!")
                return HttpResponseRedirect(reverse('welcome'))
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            messages.warning(request, "Invalid login details given")
            return HttpResponseRedirect(reverse('welcome'))
    else:
        return render(request, 'student/login.html', {})

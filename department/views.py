from ast import Delete
from django.shortcuts import render
from django.contrib import messages
from department.forms import DepForm,DepProfileInfoForm, CourseAddForm, NotForm, FacForm, FacultyForm, TeachesForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from department.models import CourseInfo, DepProfileInfo, Notification, Faculty, Teaches, ProgramInfo
from student.models import Enroll, StudentInfo
import os
import mimetypes


#@login_required(login_url='/')
def index(request):
    registered = False
    if request.method == 'POST':
        depinf = DepProfileInfo.objects.get(user=request.user)
        course_form = CourseAddForm(request.POST, request.FILES)
        if course_form.is_valid():
            course = course_form.save(commit=False)
            course.department=depinf
            course.save()
            seatadjsut()
            registered = True
            
        else:
            print(course_form.errors)
    else:
        course_form = CourseAddForm()
    
    registered = False
    if request.method == 'POST':
        f_user_form = FacForm(data=request.POST)
        f_profile_form = FacultyForm(data=request.POST)
        if f_user_form.is_valid() and f_profile_form.is_valid():
            user = f_user_form.save()
            user.set_password(user.password)
            user.save()
            f_profile = f_profile_form.save(commit=False)
            f_profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                f_profile.profile_pic = request.FILES['profile_pic']
            f_profile.save()
            registered = True
        else:
            print(f_user_form.errors,f_profile_form.errors)
    else:
        f_user_form = FacForm()
        f_profile_form = FacultyForm()
    
    if request.method == 'POST':
        depinf = DepProfileInfo.objects.get(user=request.user)
        nots_form = NotForm(data=request.POST)
        if nots_form.is_valid():
            
            nots = nots_form.save(commit=False)
            nots.department = depinf
            nots.save()
            nots_form = NotForm()
            registered = True
        else:
            print(nots_form.errors)
    else:
        nots_form = NotForm()

    if request.method == 'POST':
        
        tc_form = TeachesForm(data=request.POST)
        if tc_form.is_valid():
            
            tc = tc_form.save(commit=False)
            
            tc.save()
            registered = True
        else:
            print(tc_form.errors)
    else:
        tc_form = TeachesForm()
    
    if request.user.is_authenticated:
        depinf = DepProfileInfo.objects.get(user=request.user)
        cour = CourseInfo.objects.filter(department=depinf)
        notsin = Notification.objects.filter(department=depinf)
        student = StudentInfo.objects.filter(department=depinf)
        staff = Faculty.objects.filter(department=depinf)
        teaches = Teaches.objects.all()
        teach=[]
        for tch in teaches:
            if tch.course.department==depinf:
                teach.append(tch)
        enrolled = Enroll.objects.all()
        en_lst=[]
        for enr in enrolled:
            if enr.course.department==depinf:
                en_lst.append(enr)


        f_no_list =[st for st in staff if st not in [t.faculty for t in teaches]]
        c_no_list =[cs for cs in cour if cs not in [c.course for c in teaches]]
        course_form = CourseAddForm()
        f_user_form = FacForm()
        f_profile_form = FacultyForm()
        tc_form = TeachesForm()
        nots_form = NotForm()
        return render(request,'department/index.html', {'enrolled': en_lst,'teaches': teach, 'c_no_list': c_no_list,'f_no_list': f_no_list, 'tc_form':tc_form,'depinf':depinf,'notsin':notsin, 'cour': cour, 'course_form':course_form, 'nots_form': nots_form, 'student':student, 'f_user_form': f_user_form, 'f_profile_form': f_profile_form, 'staff': staff})




def welcome(request):
    deps=DepProfileInfo.objects.all()
    nots4 = Notification.objects.all().order_by('-id')[:4]
    nots = Notification.objects.all().order_by('-id')[4:]
    progs = ProgramInfo.objects.all()
    r=[]
    for d in deps:
        c = CourseInfo.objects.filter(department=d.id)
        r.append({'dep':d, 'cor':c})

    return render(request,'department/welcome.html', context={'progs':progs,'r':r, 'nots': nots, 'nots4':nots4, 'deps':deps  })


@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('welcome'))

def approve_student(request, student_id):
    student = User.objects.get(id=student_id)
    info = StudentInfo.objects.get(user=student)
    info.approved=True
    info.save()
    return HttpResponseRedirect(reverse('index'))

def approve_all(request):
    dep = DepProfileInfo.objects.get(user=request.user)
    st = StudentInfo.objects.filter(department=dep)
    for s in st:
        s.approved=True
        s.save()
    return HttpResponseRedirect(reverse('index'))

def reject_student(request, student_id):
    student = User.objects.get(id=student_id)
    info = StudentInfo.objects.get(user=student)
    info.delete()
    student.delete()
    return HttpResponseRedirect(reverse('index'))

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
            dep0 = User(username=username, email=email, is_staff=1)
            dep0.set_password(password)
            dep0.save()

            phone = request.POST.get('phone')
            department_name = request.POST.get('department_name')
            bio = request.POST.get('bio')
            website = request.POST.get('website')
            st_inf = DepProfileInfo(phone=phone, department_name=department_name, user_id=dep0.id, bio=bio, website=website)
            st_inf.save()
            messages.success(request, "Regitration Success!")
            return HttpResponseRedirect(reverse('welcome'))
        else: 
            messages.warning(request, "Username or email already exist!")
            return HttpResponseRedirect(reverse('welcome'))

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
                messages.warning(request, "You are not a Department!")
                return HttpResponseRedirect(reverse('welcome'))
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            messages.warning(request, "Invalid login details given")
            return HttpResponseRedirect(reverse('welcome'))
    else:
        return HttpResponseRedirect(reverse('welcome'))

def courseAdd(request):
    registered = False
    if request.method == 'POST':
        course_form = CourseAddForm(request.POST, request.FILES)
        if course_form.is_valid():
            
            course = course_form.save(commit=False)
            course.save()
            registered = True
            
        else:
            print(course_form.errors)
    else:
        course_form = CourseAddForm()
    seatadjsut()
    return render(request,'department/',
                          {
                           'course_form':course_form,
                           'registered':registered})

def seatadjsut():
    c = CourseInfo.objects.all().order_by('-id')[0]
    print(c)
    c.seats_left = c.no_of_seats
    c.save()

def courseDel(request, course_id):
    print(course_id)
    crs=CourseInfo.objects.get(id=course_id)
    crs.delete()
    
    return HttpResponseRedirect(reverse('index'))

def notDel(request, not_id):
    nt=Notification.objects.get(id=not_id)
    nt.delete()
    return HttpResponseRedirect(reverse('index'))

def unEnroll(request, enroll_id):
    enroled = Enroll.objects.get(id=enroll_id)
    enroled.delete()
    cor = CourseInfo.objects.get(id=enroled.course.id)
    cor.seats_left+=1
    cor.save()
    return HttpResponseRedirect(reverse('index'))

def downloadSyl(request, course_id):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    corse= CourseInfo.objects.get(id=course_id)
    paths = corse.syllabus.url
    filepath = BASE_DIR + paths
    #path = open(filepath, 'r', encoding='utf-8')
    with open(filepath, 'rb') as f:
        path = f.read()
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s.pdf" % "syllabus"
    # Return the response value
    return response

def enrollInfo(request):
    dep = DepProfileInfo.objects.get(user_id=request.user.id)
    enrol = Enroll.objects.all()
    enr_dep=[]
    for en_s in enrol:
        if en_s.student.department == dep:
            enr_dep.append(en_s)
    return render(request,'department/EnrollData.html', {'enroll':enr_dep, 'dep':dep })

def StudentRegInfo(request):
    dep = DepProfileInfo.objects.get(user_id=request.user.id)
    enrol = Enroll.objects.all()
    enr_dep=[]
    for en_s in enrol:
        if en_s.course.department == dep:
            enr_dep.append(en_s)
    return render(request,'department/DepStudents.html', {'student':enr_dep, 'dep': dep })



from django.shortcuts import render
from myApp.models import *


def StudentPage(request):
    if request.method=="POST":
        student_name=request.POST.get('name')
        email_name=request.POST.get('email')
        contact_no=request.POST.get('contact')
        student_age=request.POST.get('age')
        city_name=request.POST.get('city')

        student=StudentModel(
            Name=student_name,
            Email=email_name,
            Contact=contact_no,
            Age=student_age,
            City=city_name,
        )
        student.save()

    studentdata=StudentModel.objects.all()
    return render(request, 'student.html', {'data':studentdata})


def TeacherPage(request):
    if request.method=='POST':
        teacher_name=request.POST.get('name')
        email_name=request.POST.get('email')
        subject_name=request.POST.get('subject')
        department_name=request.POST.get('department')
        city_name=request.POST.get('city')

        teacher=TeacherModel(
            Name=teacher_name,
            Email=email_name,
            Subject=subject_name,
            Department=department_name,
            City=city_name,
        )
        teacher.save()
    #Show all teacher data all
    teacherdata=TeacherModel.objects.all()
    return render(request, 'teacher.html', {'data':teacherdata})

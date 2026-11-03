from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Exam
from django.db.models import Q
from django.contrib.auth.views import LoginView
from django.core.cache import cache
import logging
import json

security_logger = logging.getLogger('security')

@login_required
def addView(request):
    if request.method == 'POST':
        course = request.POST.get('course')
        date = request.POST.get('date')
        time = request.POST.get('time')
        description = request.POST.get('description')
        Exam.objects.create(
            owner = request.user,
            course = course,
            date = date,
            time = time,
            description = description
        )
    return redirect('/')

@login_required
def eraseView(request, exam_id):
    if request.method == 'POST':
        #Flaw (1): Broken Access Control
        #We don't check if the owner of the exam is the person trying to delete it
        #exam = Exam.objects.get(id=exam_id)
        #Fix:
        exam = Exam.objects.get(id=exam_id, owner = request.user)
        exam.delete()
    return redirect('/')

@login_required
def searchExamView(request):
    course = request.GET.get('course', '')
    
    #Flaw (1): Broken Accesss Control
    #We don't check who the owner is when searching exams by name
    #exams = Exam.objects.filter(course__icontains=course)
    #Fix:
    #exams = Exam.objects.filter(course__icontains=course, owner=request.user)
    
    #Flaw (3): SQL Injection
    #We are going to build a SQL query with the text introduced by the user
    #query = f"""
    #SELECT * FROM tasks_exam
    #WHERE course LIKE '%{course}%'
    #AND owner_id = {request.user.id}"""
    #exams = Exam.objects.raw(query)
    #Fix:
    #exams = Exam.objects.filter(course__icontains=course, owner=request.user)

    exams = Exam.objects.filter(course__icontains=course, owner=request.user)
    context = {'exams': exams}
    return render(request, 'pages/index.html', context)

@login_required
def homePageView(request):
    exams = Exam.objects.filter(owner=request.user)
    context = {'exams': exams}
    return render(request, 'pages/index.html', context)

#We are using this class for Flaw(5)
class SecurityLoginView(LoginView):
    def form_invalid(self, form):
        username = self.request.POST.get('username','')
        #Count failed attempts during the last minute
        key = f'login_attempts_{username}'
        attempts = cache.get(key,0)+1
        cache.set(key,attempts, timeout = 60)
        security_logger.warning("Failed login attempt. Username: %s. Attempts: %s", username, attempts)
        if attempts >= 5:
            security_logger.error(
                "ALERT: Too many failed login attempts for username: %s", username
            )
        return super().form_invalid(form)

    def form_valid(self,form):
        username = self.request.POST.get('username', '')
        cache.delete(f'login_attempts_{username}')
        return super().form_valid(form)
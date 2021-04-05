from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

from .models import DoctorProfile,UsersProfile
from .decorators import doctor_only,admin_only,doctor_and_admin
from .forms import AddNewUser

def login_page(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('projects:index')
            return HttpResponse('Your User Not Is Valid')
        else:
            return render(request, 'accounts/login.html')
    else:
       return redirect('projects:index')



def all_users(request):
    users = UsersProfile.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(users, 1)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {
        'users':users
    }
    return render(request,'accounts/users/all_users.html',context)



@admin_only
def add_new_user(request):
    if request.method == 'POST':
        form = AddNewUser(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('accounts:all_users')
    else:
        form = AddNewUser()
    context = {
        'form':form
    }
    return render(request,'accounts/users/add_new_user.html',context)








def all_doctors(request):
    doctors = DoctorProfile.objects.doctors()

    page = request.GET.get('page', 1)
    paginator = Paginator(doctors, 1)
    try:
        doctors = paginator.page(page)
    except PageNotAnInteger:
        doctors = paginator.page(1)
    except EmptyPage:
        doctors = paginator.page(paginator.num_pages)
    context = {
        'doctors':doctors
    }
    return render(request,'accounts/all_doctors.html',context)

def add_doctors(request):
    pass









def all_teaching_assistants(request):
    teaching_assistants = DoctorProfile.objects.teaching_assistants()

    page = request.GET.get('page', 1)
    paginator = Paginator(teaching_assistants, 1)
    try:
        teaching_assistants = paginator.page(page)
    except PageNotAnInteger:
        teaching_assistants = paginator.page(1)
    except EmptyPage:
        teaching_assistants = paginator.page(paginator.num_pages)
    context = {
        'teaching_assistants': teaching_assistants
    }
    return render(request, 'accounts/all_teaching_assistants.html', context)
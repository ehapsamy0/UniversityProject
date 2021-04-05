from django.http import HttpResponse
from django.shortcuts import redirect




def admin_only(func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_staff == True:
            return func(request,*args,**kwargs)
        else:
            return redirect('/')
    return wrapper


def student_only(func):
    def wrapper(request,*args,**kwargs):
        if request.user.usersprofile.student == True:
            return func(request,*args,**kwargs)
        else:
            return redirect('/')
    return wrapper


def doctor_only(func):
    def wrapper(request,*args,**kwargs):
        if request.user.usersprofile.doctors == True:
            return func(request,*args,**kwargs)
        else:
            return redirect('/')
    return wrapper


def doctor_and_admin(func):
    def wrapper(request,*args,**kwargs):
        if request.user.usersprofile.doctors == True and request.user.is_staff == True:
            return func(request,*args,**kwargs)
        else:
            return redirect('/')
    return wrapper


from django.contrib import admin

# Register your models here.
from .models import UsersProfile,StudentProfile,Specification,DoctorProfile



admin.site.register(UsersProfile)
admin.site.register(Specification)
admin.site.register(StudentProfile)
admin.site.register(DoctorProfile)
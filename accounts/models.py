from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver

from django.utils.translation import gettext as _

# Create your models here.
from django.db.models.signals import post_save, pre_save


class UsersProfile(models.Model):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('doctor', 'Doctor'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=50,null=True)
    email = models.EmailField(null=True)
    image = models.ImageField(null=True)
    student = models.BooleanField(default=False)
    doctors = models.BooleanField(default=False)
    active = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        pass


def post_save_user_profile(sender,instance,created,*args,**kwargs):
    if created:
        UsersProfile.objects.create(user=instance)
post_save.connect(post_save_user_profile,sender=User)


class StudentProfile(models.Model):
    user = models.OneToOneField(UsersProfile,on_delete=models.CASCADE)
    degree = models.IntegerField()

    def __str__(self):
        return f'{self.user.user.username}'


class Specification(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return f'{self.name}'

class DoctorsQuerySet(models.query.QuerySet):

    def active(self):
        return self.filter(user__active=True)



class DoctorsManger(models.Manager):
    def get_queryset(self):
        return DoctorsQuerySet(self.model,using=self._db)


    def doctors(self):
        return self.get_queryset().filter(teaching_assistants=False).active()

    def teaching_assistants(self):
        return self.get_queryset().filter(teaching_assistants=True).active()


class DoctorProfile(models.Model):
    user = models.OneToOneField(UsersProfile,on_delete=models.CASCADE)
    specification = models.ForeignKey(Specification,on_delete=models.SET_NULL,null=True)
    teaching_assistants = models.BooleanField(default=False)

    objects = DoctorsManger()

    def __str__(self):
        return f'{self.user.user.username}'


def pre_save_create_dctore(sender, instance, *args, **kwargs):
    user = instance
    doctor = DoctorProfile.objects.filter(user=user)
    if user.doctors and doctor.count() == 0:
        DoctorProfile.objects.create(user=instance)
    else:
        doctor.delete()

pre_save.connect(pre_save_create_dctore,sender=UsersProfile)



def pre_save_create_studen(sender,instance,*args,**kwargs):
    user = instance
    student = StudentProfile.objects.filter(user=user)
    if user.student and student.count() == 0:
        StudentProfile.objects.create(user=instance,degree=0)
    else:
        student.delete()

pre_save.connect(pre_save_create_studen,sender=UsersProfile)



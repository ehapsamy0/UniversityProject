from django.db import models
from group.models import Group
# Create your models here.
import datetime
from accounts.models import DoctorProfile

class Location(models.Model):
    name = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Lectures(models.Model):
    lectures_name = models.CharField(max_length=150)
    date_time = models.DateTimeField(default=datetime.datetime.now())
    doctor = models.ForeignKey(DoctorProfile,on_delete=models.SET_NULL,null=True)
    group = models.ForeignKey(Group,on_delete=models.SET_NULL,null=True)
    location = models.ForeignKey(Location,on_delete=models.SET_NULL,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.lectures_name
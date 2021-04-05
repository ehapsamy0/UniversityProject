from django.db import models

# Create your models here.

from accounts.models import DoctorProfile

class Project(models.Model):
    name = models.CharField(max_length=250)
    doctor = models.ForeignKey(DoctorProfile,on_delete=models.SET_NULL,null=True)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name




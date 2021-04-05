from django.db import models

# Create your models here.
from projects.models import Project
from accounts.models import StudentProfile,DoctorProfile

class Group(models.Model):
    name = models.CharField(max_length=120)
    leader = models.ForeignKey(StudentProfile,on_delete=models.SET_NULL,null=True)
    number_student = models.IntegerField()
    project = models.OneToOneField(Project,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class GroupMember(models.Model):
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    student = models.ForeignKey(StudentProfile,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.user.username} in Group {self.group.name} "


class GroupTeachingAssistants(models.Model):
    teacher = models.ForeignKey(DoctorProfile,on_delete=models.SET_NULL,null=True)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.teacher.user.username} in group {self.group.name}"


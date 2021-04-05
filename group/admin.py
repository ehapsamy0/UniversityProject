from django.contrib import admin

# Register your models here.
from .models import Group,GroupMember,GroupTeachingAssistants



admin.site.register(Group)
admin.site.register(GroupMember)
admin.site.register(GroupTeachingAssistants)

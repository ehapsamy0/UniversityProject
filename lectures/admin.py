from django.contrib import admin

# Register your models here.
from .models import Lectures,Location

admin.site.register(Lectures)
admin.site.register(Location)

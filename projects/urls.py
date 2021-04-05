from django.urls import path

from .views import index,all_projects,add_new_project,update_projects,delete_projects


app_name = 'projects'


urlpatterns = [
    path('',index,name='index'),
    path('projects/',all_projects,name='all_projects'),
    path('projects/add/',add_new_project,name='add_new_project'),
    path('projects/update/<int:id>/',update_projects,name='update_projects'),
    path('projects/delete/<int:id>/',delete_projects,name='delete_projects'),
]
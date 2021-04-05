from django.shortcuts import render,redirect,get_object_or_404
# Create your views here.
from accounts.decorators import admin_only,doctor_only,student_only,doctor_and_admin
from .models import Project
from .forms import AddProjectForm
def index(request):

    context = {

    }
    return render(request,'home/index.html',context)

@doctor_and_admin
def all_projects(request):
    projects = Project.objects.all()

    context = {
        'projects':projects
    }
    return render(request,'projects/all_projects.html',context)

@doctor_and_admin
def add_new_project(request):
    if request.method == 'POST':
        form = AddProjectForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('projects:all_projects')
    else:
        form = AddProjectForm()
    context = {
        'form':form
    }
    return render(request,'projects/add_project.html',context)

@doctor_and_admin
def update_projects(request,id):
    project = get_object_or_404(Project,id=id)
    if request.method == 'POST':
        form = AddProjectForm(request.POST or None,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects:all_projects')
    else:
        form = AddProjectForm(instance=project)
    context = {
        'form':form
    }
    return render(request,'projects/add_project.html',context)




@doctor_and_admin
def delete_projects(request,id):
    project = get_object_or_404(Project,id=id)
    project.delete()
    return redirect('projects:all_projects')

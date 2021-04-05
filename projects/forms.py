from django import forms
from .models import Project



class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name','doctor','description')
        widgets = {
            'name':forms.TextInput(attrs={
                'class':'form-control col-md-8 mb-2'}),
            'doctor':forms.Select(attrs={
                'class':'form-control col-md-8 mb-2'}),
            'description':forms.Textarea(attrs={
                'class':'form-control col-md-8 mb-2'}),

        }
        labels = {
            'name':'اسم المشروع ',
            'doctor':'اسم الدكتور المشرف ',
            'description':'الوصف الخاص بالمشروع ',
        }
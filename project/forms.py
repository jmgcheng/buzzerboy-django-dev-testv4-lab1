from django import forms
from django.core.exceptions import ValidationError
from project.models import ProjectCategory, Project, ProjectTask


class ProjectForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=ProjectCategory.objects.all(), required=True)
    class Meta:
        model = Project
        fields = ['title', 'description', 'category', 'created_at']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        }


class ProjectTaskForm(forms.ModelForm):
    class Meta:
        model = ProjectTask
        fields = ['name', 'due_date', 'priority', 'status']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        project = self.initial.get('project')
        name = cleaned_data.get('name')
        if project and name:
            if ProjectTask.objects.filter(project=project, name=name).exclude(pk=self.instance.pk).exists():
                raise ValidationError({'name': 'Task with this name already exists in this project.'})
        return cleaned_data

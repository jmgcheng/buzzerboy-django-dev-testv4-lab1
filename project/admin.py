from django.contrib import admin
from project.models import ProjectCategory, Project, ProjectTask

admin.site.register(ProjectCategory)
admin.site.register(Project)
admin.site.register(ProjectTask)
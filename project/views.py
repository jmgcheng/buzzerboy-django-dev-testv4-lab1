from django.shortcuts import render, get_object_or_404, redirect
from project.models import Project, ProjectCategory, ProjectTask
from project.forms import ProjectForm, ProjectTaskForm
from django.contrib import messages
from django.views.decorators.http import require_POST


def project_list(request):
    projects = Project.objects.all()
    data = {
        'page_title': 'Projects',
        'projects': projects,
        'menu_active': 'project',
    }
    return render(request, 'project/project_list.html', data)


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tasks = project.tasks.all().order_by('due_date')
    data = {
        'page_title': 'Project Details',
        'project': project,
        'tasks': tasks,
        'menu_active': 'project',
    }
    return render(request, 'project/project_detail.html', data)


def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project Created')
            return redirect('project-list')
    else:
        form = ProjectForm()
    data = {
        'page_title': 'Project',
        'form': form,
        'form_action': 'Create',
        'menu_active': 'project',
    }
    return render(request, 'project/project_form.html', data)


def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project Updated')
            return redirect('project-detail', pk=pk)
    else:
        form = ProjectForm(instance=project)
    data = {
        'page_title': 'Project',
        'form': form,
        'form_action': 'Update',
        'menu_active': 'project',
    }    
    return render(request, 'project/project_form.html', data)


@require_POST
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    messages.success(request, f'Project "{project.title}" deleted successfully.')
    return redirect('project-list')


def project_task_detail(request, project_pk, task_pk):
    project = get_object_or_404(Project, pk=project_pk)
    task = get_object_or_404(ProjectTask, pk=task_pk, project=project)
    data = {
        'page_title': 'Task Details',
        'project': project,
        'task': task,
        'menu_active': 'project',
    }
    return render(request, 'project/project_task_detail.html', data)


def project_task_create(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    if request.method == 'POST':
        form = ProjectTaskForm(request.POST, initial={'project': project})
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            messages.success(request, 'Project Task Created')
            return redirect('project-detail', pk=project_pk)
    else:
        form = ProjectTaskForm()
    data = {
        'page_title': 'Project Task',
        'form': form,
        'form_action': 'Create',
        'project': project,
        'menu_active': 'project',
    }
    return render(request, 'project/project_task_form.html', data)


def project_task_update(request, project_pk, task_pk):
    project = get_object_or_404(Project, pk=project_pk)
    task = get_object_or_404(ProjectTask, pk=task_pk, project=project)
    if request.method == 'POST':
        form = ProjectTaskForm(request.POST, instance=task, initial={'project': project})
        if form.is_valid():
            form.save()
            messages.success(request, 'Project Task updated successfully')
            return redirect('project-detail', pk=project_pk)
    else:
        form = ProjectTaskForm(instance=task)
    context = {
        'page_title': 'Update Project Task',
        'form': form,
        'form_action': 'Update',
        'project': project,
        'task': task,
        'menu_active': 'project',
    }
    return render(request, 'project/project_task_form.html', context)


@require_POST
def project_task_delete(request, project_pk, task_pk):
    project = get_object_or_404(Project, pk=project_pk)
    task = get_object_or_404(ProjectTask, pk=task_pk, project=project)
    task.delete()
    messages.success(request, f'Task "{task.name}" deleted successfully.')
    return redirect('project-detail', pk=project_pk)
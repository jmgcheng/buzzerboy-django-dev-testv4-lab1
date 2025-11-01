from django.urls import path, include
from project.views import project_list, project_detail, project_create, project_update, project_task_detail, project_task_create, project_task_update, project_task_delete, project_delete

urlpatterns = [
    path('', project_list, name="project-list"),
    path('<int:pk>/', project_detail, name="project-detail"),
    path('create/', project_create, name="project-create"),
    path('<int:pk>/update/', project_update, name="project-update"),

    path('<int:pk>/delete/', project_delete, name="project-delete"),

    path('<int:project_pk>/tasks/<int:task_pk>/', project_task_detail, name="project-task-detail"),
    path('<int:project_pk>/tasks/create/', project_task_create, name="project-task-create"),
    path('<int:project_pk>/tasks/<int:task_pk>/update', project_task_update, name="project-task-update"),

    path('<int:project_pk>/tasks/<int:task_pk>/delete', project_task_delete, name="project-task-delete"),

]
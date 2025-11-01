from django.db import models
from django.utils.timezone import now


class ProjectCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('CLOSED', 'Closed'),
    ]

    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    category = models.ForeignKey(ProjectCategory, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProjectTask(models.Model):
    PRIORITY_CHOICES = [
        ('HIGH', 'High'),
        ('MED', 'Medium'),
        ('LOW', 'Low'),
    ]

    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('ON_HOLD', 'On Hold'),
        ('IN_PROGRESS', 'In Progress'),
        ('REVIEW_DEV', 'Review Dev'),
        ('REVIEW_QA', 'Review QA'),
        ('DONE', 'Done'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=200)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='MED')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')
    due_date = models.DateField(null=True, blank=True)

    class Meta:
        # unique_together = ('project', 'name') in before Django 2.2
        constraints = [
            models.UniqueConstraint(fields=['project', 'name'], name='unique_task_per_project')
        ]

    def __str__(self):
        return f"{self.name} ({self.project.title})"


    

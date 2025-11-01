from django.shortcuts import render
from project.models import Project
from restaurant.models import Restaurant

def index(request):
    projects = Project.objects.all().order_by('created_at')[:5]
    restaurants = Restaurant.objects.all().order_by('establish_date')[:5]
    data = {
        'page_title': 'Homepage',
        'projects': projects,
        'restaurants': restaurants,
        'menu_active': 'homepage',
    }

    return render(request, 'page/homepage.html', data)
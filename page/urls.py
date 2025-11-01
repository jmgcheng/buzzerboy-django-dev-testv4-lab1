from django.urls import path
from page.views import index

urlpatterns = [
    path('', index, name='homepage'),
    # path('about-us', about, name='about-us'),
]

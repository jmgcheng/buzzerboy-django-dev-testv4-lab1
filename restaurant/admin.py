from django.contrib import admin
from restaurant.models import RestaurantCuisine, Restaurant, RestaurantMenu

admin.site.register(RestaurantCuisine)
admin.site.register(Restaurant)
admin.site.register(RestaurantMenu)
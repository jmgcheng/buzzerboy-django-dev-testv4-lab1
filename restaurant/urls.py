from django.urls import path, include
from restaurant.views import restaurant_list, restaurant_detail, restaurant_create, restaurant_update, restaurant_menu_detail, restaurant_menu_create, restaurant_menu_update, restaurant_menu_delete, restaurant_delete

urlpatterns = [
    path('', restaurant_list, name="restaurant-list"),
    path('<int:pk>/', restaurant_detail, name="restaurant-detail"),
    path('create/', restaurant_create, name="restaurant-create"),
    path('<int:pk>/update/', restaurant_update, name="restaurant-update"),    

    path('<int:pk>/delete/', restaurant_delete, name="restaurant-delete"),

    path('<int:restaurant_pk>/menus/<int:menu_pk>/', restaurant_menu_detail, name="restaurant-menu-detail"),
    path('<int:restaurant_pk>/menus/create/', restaurant_menu_create, name="restaurant-menu-create"),
    path('<int:restaurant_pk>/menus/<int:menu_pk>/update', restaurant_menu_update, name="restaurant-menu-update"),

    path('<int:restaurant_pk>/menus/<int:menu_pk>/delete', restaurant_menu_delete, name="restaurant-menu-delete"),

]
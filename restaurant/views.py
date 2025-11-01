from django.shortcuts import render, get_object_or_404, redirect
from restaurant.models import Restaurant, RestaurantMenu
from restaurant.forms import RestaurantForm, RestaurantMenuForm
from django.contrib import messages
from django.views.decorators.http import require_POST


def restaurant_list(request):
    restaurants = Restaurant.objects.all().order_by('-establish_date')
    data = {
        'page_title': 'Restaurants',
        'restaurants': restaurants,
        'menu_active': 'restaurant',
    }
    return render(request, 'restaurant/restaurant_list.html', data)


def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    menus = restaurant.menus.all()
    data = {
        'page_title': 'Restaurant Details',
        'restaurant': restaurant,
        'menus': menus,
        'menu_active': 'restaurant',
    }
    return render(request, 'restaurant/restaurant_detail.html', data)


def restaurant_create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Restaurant Created')
            return redirect('restaurant-list')
    else:
        form = RestaurantForm()
    data = {
        'page_title': 'Restaurant',
        'form': form,
        'form_action': 'Create',
        'menu_active': 'restaurant',
    }
    return render(request, 'restaurant/restaurant_form.html', data)


def restaurant_update(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            messages.success(request, 'Restaurant Updated')
            return redirect('restaurant-detail', pk=pk)
    else:
        form = RestaurantForm(instance=restaurant)
    data = {
        'page_title': 'Restaurant',
        'form': form,
        'form_action': 'Update',
        'menu_active': 'restaurant',
    }    
    return render(request, 'restaurant/restaurant_form.html', data)


@require_POST
def restaurant_delete(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    restaurant.delete()
    messages.success(request, f'Restaurant "{restaurant.name}" deleted successfully.')
    return redirect('restaurant-list')


def restaurant_menu_detail(request, restaurant_pk, menu_pk):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_pk)
    menu = get_object_or_404(RestaurantMenu, pk=menu_pk, restaurant=restaurant)
    data = {
        'page_title': 'Menu Details',
        'restaurant': restaurant,
        'menu': menu,
        'menu_active': 'restaurant',
    }
    return render(request, 'restaurant/restaurant_menu_detail.html', data)


def restaurant_menu_create(request, restaurant_pk):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_pk)
    if request.method == 'POST':
        form = RestaurantMenuForm(request.POST, initial={'restaurant': restaurant})
        if form.is_valid():
            menu = form.save(commit=False)
            menu.restaurant = restaurant
            menu.save()
            messages.success(request, 'Restaurant Menu Created')
            return redirect('restaurant-detail', pk=restaurant_pk)
    else:
        form = RestaurantMenuForm()
    data = {
        'page_title': 'Restaurant Menu',
        'form': form,
        'form_action': 'Create',
        'restaurant': restaurant,
        'menu_active': 'restaurant',
    }
    return render(request, 'restaurant/restaurant_menu_form.html', data)


def restaurant_menu_update(request, restaurant_pk, menu_pk):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_pk)
    menu = get_object_or_404(RestaurantMenu, pk=menu_pk, restaurant=restaurant)
    if request.method == 'POST':
        form = RestaurantMenuForm(request.POST, instance=menu, initial={'restaurant': restaurant})
        if form.is_valid():
            form.save()
            messages.success(request, 'Restaurant Menu updated successfully')
            return redirect('restaurant-detail', pk=restaurant_pk)
    else:
        form = RestaurantMenuForm(instance=menu)
    context = {
        'page_title': 'Update Restaurant Menu',
        'form': form,
        'form_action': 'Update',
        'restaurant': restaurant,
        'menu': menu,
        'menu_active': 'restaurant',
    }
    return render(request, 'restaurant/restaurant_menu_form.html', context)


@require_POST
def restaurant_menu_delete(request, restaurant_pk, menu_pk):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_pk)
    menu = get_object_or_404(RestaurantMenu, pk=menu_pk, restaurant=restaurant)
    menu.delete()
    messages.success(request, f'Menu "{menu.name}" deleted successfully.')
    return redirect('restaurant-detail', pk=restaurant_pk)    
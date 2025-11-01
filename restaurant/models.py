from django.db import models


# class RestaurantCuisine(models.Model):
#     name = models.CharField(max_length=100, unique=True)
# 
#     def __str__(self):
#         return self.name


class Restaurant(models.Model):
    CUISINE_CHOICES = [
        ('FILIPINO', 'Filipino'),
        ('JAPANESE', 'Japanese'),
        ('ITALIAN', 'Italian'),
        ('AMERICAN', 'American'),
        ('CHINESE', 'Chinese'),
        ('OTHER', 'Other'),
    ]

    STATUS_CHOICES = [
        ('OPERATIONAL', 'Operational'),
        ('CLOSED', 'Closed'),
        ('RENOVATION', 'Under Renovation'),
    ]

    name = models.CharField(max_length=200, unique=True)
    address = models.TextField()
    establish_date = models.DateField()
    # cuisine = models.ForeignKey(RestaurantCuisine, on_delete=models.SET_NULL, null=True, blank=True)
    cuisine = models.CharField(max_length=50, choices=CUISINE_CHOICES, default='OTHER')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPERATIONAL')
    capacity = models.IntegerField(default=50)

    def __str__(self):
        return self.name


class RestaurantMenu(models.Model):
    MENU_TYPE_CHOICES = [
        ('MAIN', 'Main Course'),
        ('APPETIZER', 'Appetizer'),
        ('DESSERT', 'Dessert'),
        ('DRINK', 'Drink'),
    ]

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')
    name = models.CharField(max_length=200)
    menu_type = models.CharField(max_length=20, choices=MENU_TYPE_CHOICES, default='MAIN')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.restaurant.name})"

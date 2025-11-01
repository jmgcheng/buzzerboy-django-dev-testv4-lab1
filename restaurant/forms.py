from django import forms
from django.core.exceptions import ValidationError
from restaurant.models import RestaurantCuisine, Restaurant, RestaurantMenu


class RestaurantForm(forms.ModelForm):
    cuisine = forms.ModelChoiceField(queryset=RestaurantCuisine.objects.all(), required=True)
    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'establish_date', 'cuisine', 'capacity', 'status']
        widgets = {
            'establish_date': forms.DateInput(attrs={'type': 'date'}),
        }        


class RestaurantMenuForm(forms.ModelForm):
    class Meta:
        model = RestaurantMenu
        fields = ['name', 'menu_type', 'price']

    def clean(self):
        cleaned_data = super().clean()
        restaurant = self.initial.get('restaurant')
        name = cleaned_data.get('name')
        if restaurant and name:
            if RestaurantMenu.objects.filter(restaurant=restaurant, name=name).exclude(pk=self.instance.pk).exists():
                raise ValidationError({'name': 'Menu with this name already exists in this restaurant.'})
        return cleaned_data

from django.contrib import admin
from .models import Restaurant, Menu, Dish, Review

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Dish)
admin.site.register(Review)

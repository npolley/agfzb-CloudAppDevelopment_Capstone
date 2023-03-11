from django.contrib import admin
from .models import CarMake, CarModel
# from .models import related models


# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 2

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['carMake', 'name', 'dealerID', 'carType', 'year']
    list_filter = ['carType', 'carMake', 'dealerID', 'year',]
    search_fields = ['carMake', 'name']

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ['name', "speed",'description']
    search_fields = ['name']
    inlines = [CarModelInline]

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
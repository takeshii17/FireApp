from django.contrib import admin
from .models import Incident, Locations, Firefighters, FireStation, FireTruck, WeatherConditions

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('location', 'date_time', 'severity_level', 'description')
    list_filter = ('severity_level', 'date_time')
    search_fields = ('description', 'location__name')

@admin.register(WeatherConditions)
class WeatherConditionsAdmin(admin.ModelAdmin):
    list_display = ('incident', 'temperature', 'humidity', 'wind_speed', 'weather_description')
    list_filter = ('incident__date_time',)
    search_fields = ('weather_description',)

@admin.register(Locations)
class LocationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'country')
    list_filter = ('city', 'country')
    search_fields = ('name', 'address')

@admin.register(Firefighters)
class FirefightersAdmin(admin.ModelAdmin):
    list_display = ('name', 'rank', 'experience_level', 'station')
    list_filter = ('rank', 'experience_level')
    search_fields = ('name',)

@admin.register(FireStation)
class FireStationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'country')
    list_filter = ('city', 'country')
    search_fields = ('name', 'address')

@admin.register(FireTruck)
class FireTruckAdmin(admin.ModelAdmin):
    list_display = ('truck_number', 'model', 'capacity', 'station')
    list_filter = ('station',)
    search_fields = ('truck_number', 'model')

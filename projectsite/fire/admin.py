from django.contrib import admin
from fire.models import Incident, Locations, Firefighters, FireStation, FireTruck, WeatherConditions

# admin.site.register(Incident)
@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ("location", "date_time", "severity_level", "description")

    search_fields = ("location",)

# admin.site.register(Locations)
@admin.register(Locations)
class LocationsAdmin(admin.ModelAdmin):
    list_display = ("name", "latitude", "longitude", "address", "city", "country")

    search_fields = ("name",)

# admin.site.register(Firefighters)
@admin.register(Firefighters)
class FirefightersAdmin(admin.ModelAdmin):
    list_display = ("name", "rank", "experience_level", "station")

    search_fields = ("location",)

# admin.site.register(FireStation)
@admin.register(FireStation)
class FireStationAdmin(admin.ModelAdmin):
    list_display = ("name", "latitude", "longitude", "address", "city", "country")

    search_fields = ("name",)

# admin.site.register(FireTruck)
@admin.register(FireTruck)
class FireTruckAdmin(admin.ModelAdmin):
    list_display = ("model", "truck_number", "capacity", "station")

    search_fields = ("model",)

# admin.site.register(WeatherConditions)
@admin.register(WeatherConditions)
class WeatherConditionsAdmin(admin.ModelAdmin):
    list_display = ("incident", "temperature", "humidity", "wind_speed", "weather_description")

    search_fields = ("incident",)
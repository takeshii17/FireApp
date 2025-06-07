from django.forms import ModelForm, DateInput
from .models import Locations, Incident, FireStation, Firefighters, FireTruck, WeatherConditions


class LocationsForm(ModelForm):
    class Meta:
        model = Locations
        fields = "__all__"


class IncidentForm(ModelForm):
    class Meta:
        model = Incident
        fields = "__all__"


class FireStationForm(ModelForm):
    class Meta:
        model = FireStation
        fields = "__all__"


class FirefightersForm(ModelForm):
    class Meta:
        model = Firefighters
        fields = "__all__"


class FireTruckForm(ModelForm):
    class Meta:
        model = FireTruck
        fields = "__all__"


class WeatherConditionsForm(ModelForm):
    class Meta:
        model = WeatherConditions
        fields = "__all__"

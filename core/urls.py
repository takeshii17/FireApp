from django.contrib import admin
from django.urls import path

from fire import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),

    # Locations
    path('locations/', views.LocationsList.as_view(), name='locations'),
    path('locations/add/', views.LocationsCreate.as_view(), name='locations-add'),
    path('locations/edit/<pk>/',
         views.LocationsUpdate.as_view(), name='locations-edit'),
    path('locations/delete/<pk>/',
         views.LocationsDelete.as_view(), name='locations-delete'),

    # Incident
    path('incident/', views.IncidentList.as_view(), name='incident'),
    path('incident/add/', views.IncidentCreate.as_view(), name='incident-add'),
    path('incident/edit/<pk>/',
         views.IncidentUpdate.as_view(), name='incident-edit'),
    path('incident/delete/<pk>/',
         views.IncidentDelete.as_view(), name='incident-delete'),

    # Fire Station
    path('firestation/', views.FireStationList.as_view(), name='firestation'),
    path('firestation/add/', views.FireStationCreate.as_view(),
         name='firestation-add'),
    path('firestation/edit/<pk>/',
         views.FireStationUpdate.as_view(), name='firestation-edit'),
    path('firestation/delete/<pk>/',
         views.FireStationDelete.as_view(), name='firestation-delete'),

    # Fire Fighters
    path('firefighters/', views.FirefightersList.as_view(), name='firefighters'),
    path('firefighters/add/', views.FirefightersCreate.as_view(),
         name='firefighters-add'),
    path('firefighters/edit/<pk>/',
         views.FirefightersUpdate.as_view(), name='firefighters-edit'),
    path('firefighters/delete/<pk>/',
         views.FirefightersDelete.as_view(), name='firefighters-delete'),

    # Fire Truck
    path('firetruck/', views.FireTruckList.as_view(), name='firetruck'),
    path('firetruck/add/', views.FireTruckCreate.as_view(),
         name='firetruck-add'),
    path('firetruck/edit/<pk>/',
         views.FireTruckUpdate.as_view(), name='firetruck-edit'),
    path('firetruck/delete/<pk>/',
         views.FireTruckDelete.as_view(), name='firetruck-delete'),

    # Weather Conditions
    path('weatherconditions/', views.WeatherConditionsList.as_view(),
         name='weatherconditions'),
    path('weatherconditions/add/', views.WeatherConditionsCreate.as_view(),
         name='weatherconditions-add'),
    path('weatherconditions/edit/<pk>/',
         views.WeatherConditionsUpdate.as_view(), name='weatherconditions-edit'),
    path('weatherconditions/delete/<pk>/',
         views.WeatherConditionsDelete.as_view(), name='weatherconditions-delete'),

    # Charts
    path("dashboard_chart", views.ChartView.as_view(), name="dashboard-chart"),
    path("chart/", views.PieCountSeverity, name="chart"),
    path('lineChart/', views.LineCountByMonth, name='chart'),
    path('multilineChart/', views.MultilineIncidentTop3Country, name='chart'),
    path('multiBarChart/', views.multipleBarbySeverity, name='chart'),

    # Maps
    path('stations/', views.map_station, name='map-station'),
    path('incidents/', views.map_incident, name='map-incident'),
]

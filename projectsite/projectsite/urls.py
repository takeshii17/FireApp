from django.contrib import admin
from django.urls import path

from fire.views import (
    HomePageView,
    ChartView,
    PieCountbySeverity,
    LineCountbyMonth,
    MultilineIncidentTop3Country,
    multipleBarbySeverity,
    map_station,
    map_incidents,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomePageView.as_view(), name="home"),
    path("dashboard_chart/", ChartView.as_view(), name="dashboard-chart"),
    path("chart/", PieCountbySeverity, name="pie-chart"),
    path("lineChart/", LineCountbyMonth, name="line-chart"),
    path("multilineChart/", MultilineIncidentTop3Country, name="multiline-chart"),
    path("multiBarChart/", multipleBarbySeverity, name="multibar-chart"),
    path("stations/", map_station, name="map-station"),
    path("incidents/", map_incidents, name="map-incidents"),
]

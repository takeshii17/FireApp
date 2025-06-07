from django.shortcuts import render
from django.views.generic.list import ListView
from django.db import connection
from django.http import JsonResponse
from django.db.models import Count
from datetime import datetime

from fire.models import Locations, Incident, FireStation


# Home Page View
class HomePageView(ListView):
    model = Locations
    context_object_name = "home"
    template_name = "home.html"


# Chart View
class ChartView(ListView):
    template_name = "chart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        pass


# Pie Chart Data by Severity
def PieCountbySeverity(request):
    query = """
    SELECT severity_level, COUNT(*) as count
    FROM fire_incident
    GROUP BY severity_level
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

    # Convert query result to dictionary
    data = {severity: count for severity, count in rows} if rows else {}

    return JsonResponse(data)


# Line Chart Data by Month
def LineCountbyMonth(request):
    current_year = datetime.now().year
    result = {month: 0 for month in range(1, 13)}

    incidents_per_month = Incident.objects.filter(date_time__year=current_year).values_list("date_time", flat=True)

    for date_time in incidents_per_month:
        if date_time:
            result[date_time.month] += 1

    # Map month numbers to names
    month_names = {
        1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
        7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
    }

    result_with_month_names = {month_names[month]: count for month, count in result.items()}
    return JsonResponse(result_with_month_names)


# Multiline Chart Data for Top 3 Countries
def MultilineIncidentTop3Country(request):
    query = """
    SELECT fl.country, strftime('%m', fi.date_time) AS month, COUNT(fi.id) AS incident_count
    FROM fire_incident fi
    JOIN fire_locations fl ON fi.location_id = fl.id
    WHERE fl.country IN (
        SELECT fl_top.country
        FROM fire_incident fi_top
        JOIN fire_locations fl_top ON fi_top.location_id = fl_top.id
        WHERE strftime('%Y', fi_top.date_time) = strftime('%Y', 'now')
        GROUP BY fl_top.country
        ORDER BY COUNT(fi_top.id) DESC
        LIMIT 3
    )
    AND strftime('%Y', fi.date_time) = strftime('%Y', 'now')
    GROUP BY fl.country, month
    ORDER BY fl.country, month
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

    result = {}
    months = {str(i).zfill(2) for i in range(1, 13)}

    for country, month, total_incidents in rows:
        if country not in result:
            result[country] = {m: 0 for m in months}
        result[country][month] = total_incidents

    while len(result) < 3:
        result[f"Country {len(result) + 1}"] = {month: 0 for month in months}

    for country in result:
        result[country] = dict(sorted(result[country].items()))

    return JsonResponse(result)


# Multiple Bar Chart Data by Severity
def multipleBarbySeverity(request):
    query = """
    SELECT fi.severity_level, strftime('%m', fi.date_time) AS month, COUNT(fi.id) AS incident_count
    FROM fire_incident fi
    GROUP BY fi.severity_level, month
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

    result = {}
    months = {str(i).zfill(2) for i in range(1, 13)}

    for level, month, total_incidents in rows:
        level = str(level)
        if level not in result:
            result[level] = {m: 0 for m in months}
        result[level][month] = total_incidents

    for level in result:
        result[level] = dict(sorted(result[level].items()))

    return JsonResponse(result)


# Map Fire Stations
def map_station(request):
    fire_stations = FireStation.objects.values("name", "latitude", "longitude")
    fire_stations_list = [
        {
            "name": station["name"],
            "latitude": float(station["latitude"]),
            "longitude": float(station["longitude"]),
        }
        for station in fire_stations
    ]
    return render(request, "map_station.html", {"fireStations": fire_stations_list})


# Map Incidents
def map_incidents(request):
    incidents = Incident.objects.select_related("location").values(
        "location__name", "location__latitude", "location__longitude",
        "date_time", "severity_level", "description"
    )

    incidents_list = [
        {
            "name": incident["location__name"],
            "latitude": float(incident["location__latitude"]),
            "longitude": float(incident["location__longitude"]),
            "date_time": incident["date_time"].strftime("%Y-%m-%d %H:%M:%S") if incident["date_time"] else "N/A",
            "severity_level": incident["severity_level"],
            "description": incident["description"],
        }
        for incident in incidents
    ]
    return render(request, "map_incidents.html", {"fireIncidents": incidents_list})

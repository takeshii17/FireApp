from .models import Incident
from .forms import LocationsForm, IncidentForm, FireStationForm, FirefightersForm, FireTruckForm, WeatherConditionsForm
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from fire.models import Locations, Incident, FireStation, Firefighters, FireTruck, WeatherConditions
from django.db import connection
from django.db.models import Q
from django.http import JsonResponse
from django.db.models.functions import ExtractMonth
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.timezone import localtime
from django.utils.dateparse import parse_datetime

from django.db.models import Count
from datetime import datetime, timezone


class HomePageView(ListView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        pass


class LocationsList(ListView):
    model = FireStation
    context_object_name = 'locations'
    template_name = 'locations/list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(name__icontains=query))
        return qs


class LocationsCreate(CreateView):
    model = Locations
    form_class = LocationsForm
    template_name = 'locations/add.html'
    success_url = reverse_lazy('locations')

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, f'{name} has been successfully added.')
        return super().form_valid(form)


class LocationsUpdate(UpdateView):
    model = Locations
    form_class = LocationsForm
    template_name = 'locations/edit.html'
    success_url = reverse_lazy('locations')

    def form_valid(self, form):
        name = form.instance.name
        messages.success(
            self.request, f'{name} has been successfully updated.')
        return super().form_valid(form)


class LocationsDelete(DeleteView):
    model = Locations
    template_name = 'locations/delete.html'
    success_url = reverse_lazy('locations')

    def form_valid(self, form):
        messages.success(self.request, f'Deleted successfully.')
        return super().form_valid(form)


class IncidentList(ListView):
    model = Incident
    context_object_name = 'incident'
    template_name = 'incident/list.html'
    paginate_by = 5


class IncidentCreate(CreateView):
    model = Incident
    form_class = IncidentForm
    template_name = 'incident/add.html'
    success_url = reverse_lazy('incident')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        date_time = request.POST.get("date_time")
        current_date_time = timezone.now()

        # Validate date_time
        if date_time > current_date_time:
            messages.error(request, "Future dates are not allowed")

            return self.form_invalid(self.get_form())

        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        name = form.instance
        messages.success(self.request, f'{name} has been successfully added.')
        return super().form_valid(form)


class IncidentUpdate(UpdateView):
    model = Incident
    form_class = IncidentForm
    template_name = 'incident/edit.html'
    success_url = reverse_lazy('incident')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        date_time = parse_datetime(request.POST.get("date_time")).astimezone()
        current_date_time = localtime().astimezone()

        # Validate date_time
        if date_time > current_date_time:
            messages.error(request, "Future dates are not allowed")

            return self.form_invalid(self.get_form())

        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        name = form.instance
        messages.success(
            self.request, f'{name} has been successfully updated.')
        return super().form_valid(form)


class IncidentDelete(DeleteView):
    model = Incident
    template_name = 'incident/delete.html'
    success_url = reverse_lazy('incident')

    def form_valid(self, form):
        messages.success(self.request, f'Deleted successfully.')
        return super().form_valid(form)


class FireStationList(ListView):
    model = FireStation
    context_object_name = 'firestation'
    template_name = 'firestation/list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(name__icontains=query))
        return qs


class FireStationCreate(CreateView):
    model = FireStation
    form_class = FireStationForm
    template_name = 'firestation/add.html'
    success_url = reverse_lazy('firestation')

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, f'{name} has been successfully added.')
        return super().form_valid(form)


class FireStationUpdate(UpdateView):
    model = FireStation
    form_class = FireStationForm
    template_name = 'firestation/edit.html'
    success_url = reverse_lazy('firestation')

    def form_valid(self, form):
        name = form.instance.name
        messages.success(
            self.request, f'{name} has been successfully updated.')
        return super().form_valid(form)


class FireStationDelete(DeleteView):
    model = FireStation
    template_name = 'firestation/delete.html'
    success_url = reverse_lazy('firestation')

    def form_valid(self, form):
        messages.success(self.request, f'Deleted successfully.')
        return super().form_valid(form)


class FirefightersList(ListView):
    model = Firefighters
    context_object_name = 'firefighters'
    template_name = 'firefighters/list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(name__icontains=query))
        return qs


class FirefightersCreate(CreateView):
    model = Firefighters
    form_class = FirefightersForm
    template_name = 'firefighters/add.html'
    success_url = reverse_lazy('firefighters')

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, f'{name} has been successfully added.')
        return super().form_valid(form)


class FirefightersUpdate(UpdateView):
    model = Firefighters
    form_class = FirefightersForm
    template_name = 'firefighters/edit.html'
    success_url = reverse_lazy('firefighters')

    def form_valid(self, form):
        name = form.instance.name
        messages.success(
            self.request, f'{name} has been successfully updated.')
        return super().form_valid(form)


class FirefightersDelete(DeleteView):
    model = Firefighters
    template_name = 'firefighters/delete.html'
    success_url = reverse_lazy('firefighters')

    def form_valid(self, form):
        messages.success(self.request, f'Deleted successfully.')
        return super().form_valid(form)


class FireTruckList(ListView):
    model = FireTruck
    context_object_name = 'firetruck'
    template_name = 'firetruck/list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(truck_number__icontains=query))
        return qs


class FireTruckCreate(CreateView):
    model = FireTruck
    form_class = FireTruckForm
    template_name = 'firetruck/add.html'
    success_url = reverse_lazy('firetruck')

    def form_valid(self, form):
        name = form.instance
        messages.success(self.request, f'{name} has been successfully added.')
        return super().form_valid(form)


class FireTruckUpdate(UpdateView):
    model = FireTruck
    form_class = FireTruckForm
    template_name = 'firetruck/edit.html'
    success_url = reverse_lazy('firetruck')

    def form_valid(self, form):
        name = form.instance
        messages.success(
            self.request, f'{name} has been successfully updated.')
        return super().form_valid(form)


class FireTruckDelete(DeleteView):
    model = FireTruck
    template_name = 'firetruck/delete.html'
    success_url = reverse_lazy('firetruck')

    def form_valid(self, form):
        messages.success(self.request, f'Deleted successfully.')
        return super().form_valid(form)


class WeatherConditionsList(ListView):
    model = WeatherConditions
    context_object_name = 'weatherconditions'
    template_name = 'weatherconditions/list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(truck_number__icontains=query))
        return qs


class WeatherConditionsCreate(CreateView):
    model = WeatherConditions
    form_class = WeatherConditionsForm
    template_name = 'weatherconditions/add.html'
    success_url = reverse_lazy('weatherconditions')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        temperature = request.POST.get('temperature')
        humidity = request.POST.get('humidity')
        wind_speed = request.POST.get('wind_speed')

        # Validate values
        errors = []
        for field_name, value in [('temperature', temperature), ('humidity', humidity), ('wind_speed', wind_speed)]:
            try:
                if float(value) < 0:
                    errors.append(
                        f"{field_name.capitalize()} must not be a negative number.")
            except (ValueError, TypeError):
                errors.append(
                    f"{field_name.capitalize()} must be a valid non-negative number.")

        # If errors exist, display them and return to the form
        if errors:
            for error in errors:
                messages.error(request, error)
            return self.form_invalid(self.get_form())

        # Call the parent's post() if validation passes
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        name = form.instance
        messages.success(self.request, f'{name} has been successfully added.')
        return super().form_valid(form)


class WeatherConditionsUpdate(UpdateView):
    model = WeatherConditions
    form_class = WeatherConditionsForm
    template_name = 'weatherconditions/edit.html'
    success_url = reverse_lazy('weatherconditions')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        temperature = request.POST.get('temperature')
        humidity = request.POST.get('humidity')
        wind_speed = request.POST.get('wind_speed')

        # Validate values
        errors = []
        for field_name, value in [('temperature', temperature), ('humidity', humidity), ('wind_speed', wind_speed)]:
            try:
                if float(value) < 0:
                    errors.append(
                        f"{field_name.capitalize()} must be a non-negative negative number.")
            except (ValueError, TypeError):
                errors.append(
                    f"{field_name.capitalize()} must be a valid non-negative number.")

        # If errors exist, display them and return to the form
        if errors:
            for error in errors:
                messages.error(request, error)
            return self.form_invalid(self.get_form())

        # Call the parent's post() if validation passes
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        name = form.instance
        messages.success(
            self.request, f'{name} has been successfully updated.')
        return super().form_valid(form)


class WeatherConditionsDelete(DeleteView):
    model = WeatherConditions
    template_name = 'weatherconditions/delete.html'
    success_url = reverse_lazy('weatherconditions')

    def form_valid(self, form):
        messages.success(self.request, f'Deleted successfully.')
        return super().form_valid(form)


class ChartView(ListView):
    template_name = 'chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        pass


def PieCountSeverity(request):
    query = '''
    SELECT severity_level, COUNT(*) as count
    FROM fire_incident
    GROUP BY severity_level
    '''
    data = {}
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

    if rows:
        #  Construct the dictionary with severity level as keys and count as values
        data = {severity: count for severity, count in rows}
    else:
        data = {}

    return JsonResponse(data)


def LineCountByMonth(request):
    current_year = datetime.now().year

    incidents_per_month = (
        Incident.objects.filter(date_time__year=current_year)
        .annotate(month=ExtractMonth('date_time'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )

    result = {month: 0 for month in range(1, 13)}

    for item in incidents_per_month:
        result[item['month']] = item['count']

    month_names = {
        1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
        7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
    }

    result_with_month_names = {
        month_names[month]: count for month, count in result.items()
    }

    return JsonResponse(result_with_month_names)


def MultilineIncidentTop3Country(request):

    query = '''
    SELECT
        fl.country,
        strftime('%m', fi.date_time) AS month,
        COUNT(fi.id) AS incident_count
    FROM
        fire_incident fi
    JOIN
        fire_locations fl ON fi.location_id = fl.id
    WHERE
        fl.country IN (
            SELECT
                fl_top.country
            FROM
                fire_incident fi_top
            JOIN
                fire_locations fl_top ON fi_top.location_id = fl_top.id
            WHERE
                strftime('%Y', fi_top.date_time) = strftime('%Y', 'now')
            GROUP BY
                fl_top.country
            ORDER BY
                COUNT(fi_top.id) DESC
            LIMIT 3
        )   
        AND strftime('%Y', fi.date_time) = strftime('%Y', 'now')
    GROUP BY
        fl.country, month
    ORDER BY
        fl.country, month;
    '''

    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

    # Initialize a dictionary to store the result
    result = {}

    # Initialize a set of months from January to December
    months = set(str(i).zfill(2) for i in range(1, 13))

    # Loop through the query results
    for row in rows:
        country = row[0]
        month = row[1]
        total_incidents = row[2]

        # If the country is not in the result dictionary, initialize it with all months set to zero
        if country not in result:
            result[country] = {month: 0 for month in months}

        # Update the incidents count for the corresponding month
        result[country][month] = total_incidents

    # Ensure there are always 3 countries in the result
    while len(result) < 3:
        # Placeholder name for missing countries
        missing_country = f"Country {len(result) + 1}"
        result[missing_country] = {month: 0 for month in months}

    for country in result:
        result[country] = dict(sorted(result[country].items()))

    return JsonResponse(result)


def multipleBarbySeverity(request):
    query = '''
    SELECT
        fi.severity_level,
        strftime('%m', fi.date_time) AS month,
        COUNT(fi.id) AS incident_count
    FROM
        fire_incident fi
    GROUP BY fi.severity_level, month
    '''

    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

    result = {}
    months = {str(i).zfill(2)
              for i in range(1, 13)}  # Ensure all months are included

    for row in rows:
        severity_level = row[0]
        month = row[1]
        count = row[2]

        if severity_level not in result:
            result[severity_level] = {month: 0 for month in months}

        result[severity_level][month] = count

    # Sort months within each severity level
    for severity_level in result:
        result[severity_level] = dict(sorted(result[severity_level].items()))

    return JsonResponse(result)


def map_station(request):
    fireStations = FireStation.objects.values('name', 'latitude', 'longitude')

    for fireStation in fireStations:
        fireStation['latitude'] = float(fireStation['latitude'])
        fireStation['longitude'] = float(fireStation['longitude'])

    fireStations_list = list(fireStations)

    context = {
        'fireStations': fireStations_list,
    }

    return render(request, 'map_station.html', context)


def map_incident(request):
    city = request.GET.get('city', None)

    incidents_query = Incident.objects.select_related('location').all()

    if city:
        incidents_query = incidents_query.filter(
            location__city__icontains=city
        )

    incidents_list = [
        {
            'name': incident.location.name,
            'latitude': float(incident.location.latitude),
            'longitude': float(incident.location.longitude),
            'description': incident.description,
            'city': incident.location.city,
        }
        for incident in incidents_query
    ]

    cities = Locations.objects.values("city").distinct()

    context = {
        'incidents': incidents_list,
        'current_city': city,
        'cities': cities
    }

    return render(request, 'map_incident.html', context)

from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def validate_not_future(value):
    if value > timezone.now():
        raise ValidationError('Date cannot be in the future.')


def validate_non_negative(value):
    if value < 0:
        raise ValidationError('Value cannot be negative.')


class Locations(BaseModel):
    name = models.CharField(max_length=150)
    latitude = models.DecimalField(
        max_digits=22, decimal_places=16, null=True, blank=True)
    longitude = models.DecimalField(
        max_digits=22, decimal_places=16, null=True, blank=True)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Location'

    def __str__(self):
        return f"{self.name} - {self.city}, {self.country}"


class Incident(BaseModel):
    SEVERITY_CHOICES = (
        ('Minor Fire', 'Minor Fire'),
        ('Moderate Fire', 'Moderate Fire'),
        ('Major Fire', 'Major Fire'),
    )
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    date_time = models.DateTimeField(
        blank=True, null=True, validators=[validate_not_future])
    severity_level = models.CharField(max_length=45, choices=SEVERITY_CHOICES)
    description = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.severity_level} at {self.location.name} - {self.date_time}"

    class Meta:
        verbose_name = 'Incident'


class FireStation(BaseModel):
    name = models.CharField(max_length=150)
    latitude = models.DecimalField(
        max_digits=22, decimal_places=16, null=True, blank=True)
    longitude = models.DecimalField(
        max_digits=22, decimal_places=16, null=True, blank=True)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Fire Station'

    def __str__(self):
        return f"{self.name} - {self.city}"


class Firefighters(BaseModel):
    XP_CHOICES = (
        ('Probationary Firefighter', 'Probationary Firefighter'),
        ('Firefighter I', 'Firefighter I'),
        ('Firefighter II', 'Firefighter II'),
        ('Firefighter III', 'Firefighter III'),
        ('Driver', 'Driver'),
        ('Captain', 'Captain'),
        ('Battalion Chief', 'Battalion Chief'),)
    name = models.CharField(max_length=150)
    rank = models.CharField(max_length=150)
    experience_level = models.CharField(max_length=150, choices=XP_CHOICES)
    station = models.ForeignKey(
        FireStation, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Firefighter'

    def __str__(self):
        return f"{self.name} - {self.rank}"


class FireTruck(BaseModel):
    truck_number = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    capacity = models.CharField(max_length=150)
    station = models.ForeignKey(FireStation, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Fire Truck'

    def __str__(self):
        return f"Truck {self.truck_number} - {self.model}"


class WeatherConditions(BaseModel):
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE)
    temperature = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[validate_non_negative])
    humidity = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[validate_non_negative])
    wind_speed = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[validate_non_negative])
    weather_description = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Weather Condition'

    def __str__(self):
        return f"Weather for {self.incident} - {self.weather_description}"

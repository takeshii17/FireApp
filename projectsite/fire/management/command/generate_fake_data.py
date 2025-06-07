import random
from django.core.management.base import BaseCommand
from faker import Faker
from fire.models import Locations, Incident, FireStation, Firefighters, FireTruck, WeatherConditions
from django.utils import timezone


class Command(BaseCommand):
    help = 'Generates fake data for fire-related models'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create fake Locations
        for _ in range(10):
            location = Locations.objects.create(
                name=fake.company(),
                latitude=fake.latitude(),
                longitude=fake.longitude(),
                address=fake.address(),
                city=fake.city(),
                country=fake.country()
            )
            self.stdout.write(self.style.SUCCESS(
                f"Created Location: {location.name}"))

        # Create fake FireStations
        for _ in range(5):
            fire_station = FireStation.objects.create(
                name=fake.company(),
                latitude=fake.latitude(),
                longitude=fake.longitude(),
                address=fake.address(),
                city=fake.city(),
                country=fake.country()
            )
            self.stdout.write(self.style.SUCCESS(
                f"Created FireStation: {fire_station.name}"))

        # Create fake Firefighters
        for _ in range(20):
            firefighter = Firefighters.objects.create(
                name=fake.name(),
                rank=random.choice([rank[0]
                                   for rank in Firefighters.XP_CHOICES]),
                experience_level=fake.random_element(
                    elements=("Beginner", "Intermediate", "Expert")),
                station=random.choice(FireStation.objects.all())
            )
            self.stdout.write(self.style.SUCCESS(
                f"Created Firefighter: {firefighter.name}"))

        # Create fake FireTrucks
        fire_stations = FireStation.objects.all()
        for _ in range(10):
            fire_truck = FireTruck.objects.create(
                truck_number=fake.unique.bothify(text="TRK-####"),
                model=fake.word(),
                # Water capacity in liters
                capacity=fake.random_number(digits=4),
                station=random.choice(fire_stations)
            )
            self.stdout.write(self.style.SUCCESS(
                f"Created FireTruck: {fire_truck.truck_number}"))

        # Create fake Incidents
        locations = Locations.objects.all()
        for _ in range(15):
            incident = Incident.objects.create(
                location=random.choice(locations),
                date_time=fake.date_this_year(),
                severity_level=random.choice(
                    [level[0] for level in Incident.SEVERITY_CHOICES]),
                description=fake.text(max_nb_chars=250)
            )
            self.stdout.write(self.style.SUCCESS(
                f"Created Incident: {incident.description[:50]}..."))

        # Create fake WeatherConditions
        incidents = Incident.objects.all()
        for _ in range(10):
            weather_condition = WeatherConditions.objects.create(
                incident=random.choice(incidents),
                temperature=fake.random_number(digits=2),
                humidity=fake.random_number(digits=2),
                wind_speed=fake.random_number(digits=2),
                weather_description=fake.word()
            )
            self.stdout.write(self.style.SUCCESS(
                f"Created WeatherCondition for Incident: {weather_condition.incident.description[:50]}..."))

        self.stdout.write(self.style.SUCCESS("Fake data generation complete."))
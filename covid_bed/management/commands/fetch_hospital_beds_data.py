from django.core.management.base import BaseCommand
from covid_bed.utility import api_data

class Command(BaseCommand):
    help = "To get Country and India Latitude and Longitude.. run python manage.py get_lat_lon"

    def handle(self, *args, **options):
        api_data()
        print("Done")

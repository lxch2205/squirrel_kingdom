import csv

from django.core.management.base import BaseCommand
from sightings.models import Squirrel


class Command(BaseCommand):
    def add_srguments(self, parser):
        parser.add_argument('database')

    def handle(self, *args, **options):
        csv_file = list()
        for item in Squirrel.objects.all():
            csv_file.append(
                {'Latitude':item.latitude,
                'Longitude':item.longitude,
                'Unique Squirrel id':item.id,
                'Shift':item.shift,
                'Date':item.date,
                'Age':item.age,
                'Primary Fur Color':item.color,
                'Location':item.location,
                'Specific Location':item.specific_location,
                'Running':item.running,
                'Chasing':item.chasing,
                'Climbing':item.climbing,
                'Eating':item.eating,
                'Foraging':item.foraging,
                'Other Activities':item.other_activities,
                'Kuks':item.kuks,
                'Quaas':item.quaas,
                'Moans':item.moans,
                'Tail Flag':item.tail_flag,
                'Tail Twitches':item.tail_twitches,
                'Approaches':item.approaches,
                'Indifferent':item.indifferent,
                'Runs From':item.runs_from}
             )
        file_export = pd.DataFrame(csv_export)
        file_export.to_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')


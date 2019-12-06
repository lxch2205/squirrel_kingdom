from django.core.management.base import BaseCommand
from sightings.models import Squirrel

import csv

class Command(BaseCommand):
    def add_srguments(self,parser):
        parser.add_argument('database')

    def handle(self, *args, **options):
        csv_file = list()
        for item in Squirrel.objects.all():
            csv_file.append(
                {'Latitude':item.latitude,
                'Longitude':item.longitude,
                'Squirrel_id':item.squirrel_id,
                'Shift':item.shift,
                'Date':item.date,
                'Age':item.age,
                'Color':item.color,
                'Location':item.location,
                'Specific_location':item.specific_location,
                'Running':item.running,
                'Chasing':item.chasing,
                'Climbing':item.climbing,
                'Eating':item.eating,
                'Foraging':item.foraging,
                'Other_activities':item.other_activities,
                'Kuks':item.kuks,
                'Quaas':item.quaas,
                'Moans':item.moans,
                'Tail_flag':item.tail_flag,
                'Tail_twitches':item.tail_twitches,
                'Approaches':item.approaches,
                'Indifferent':item.indifferent,
                'Runs_from':item.runs_from}
            )


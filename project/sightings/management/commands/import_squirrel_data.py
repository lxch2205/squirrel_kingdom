from django.core.management.base import BaseCommand
from django.utils import timezone
from sightings.models import Squirrel

import csv
import pandas as pd

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
    
    def handle(self, *args, **options):
        df = pd.read_csv(options['csv_file'])
        for item in df.iterrows():
            item = item[1]
            s = Squirrel(
                latitude = item['Y'],
                longitude = item['X'],
                id = item['Unique Squirrel ID'],
                shift = item['Shift'],
                date = timezone.datetime(int(str(item['Date'])[-4:]),int(str(item['Date'])[-1:]),int(str(item['Date'])[2:4])).date(),
                age = item['Age'],
                color = item['Primary Fur Color'],
                location = item['Location'],
                specific_location = item['Specific Location'],
                running = item['Running'],
                chasing = item['Chasing'],
                climbing = item['Climbing'],
                eating = item['Eating'],
                foraging = item['Foraging'],
                other_activities = item['Other Activities'],
                kuks = item['Kuks'],
                quaas = item['Quaas'],
                moans = item['Moans'],
                tail_flags = item['Tail flags'],
                tail_twitches = item['Tail twitches'],
                approaches = item['Approaches'],
                indifferent = item['Indifferent'],
                runs_from = item['Runs from'],
            )
            s.save()





import csv
import datetime as dt

from django.core.management.base import BaseCommand
from sightings.models import Squirrel

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
    
    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        for item in data:
            s = Squirrel(
                latitude = item['Y'],
                longitude = item['X'],
                id = item['Unique Squirrel ID']
                shift = item['Shift']
                date = dt.datetime.striptime(data_object['Date'].strip(),'%m%d%Y').date()
                age = item['Age']
                color = item['Primary Fur Color']
                location = item['Location']
                specific_location = item['Specific Location']
                running_orig = item['Running']
                running = True if "true" in running_orig.lower() else False
                
                chasing_orig = item['Chasing']
                chasing = True if "true" in chasing_orig.lower() else False
                
                climbing_orig = item['Climbing']
                climbing = True if "true" in climbing_orig.lower() else False
                
                eating_orig = item['Eating']
                eating = True if "true" in eating_orig.lower() else False
                
                foraging_orig = item['Foraging']
                foraging = True if "true" in foraging_orig.lower() else False
                
                other_activities = item['Other Activities']
                
                kuks_orig = item['Kuks']
                kuks = True if "true" in kuks_orig.lower() else False
                
                quaas_orig = item['Quaas']
                quaas = True if "tr'e" in quaas_orig.lower() else False
                
                moans_orig = item['Moans']
                moans = True if "true" in moans_orig.lower() else False
                
                tail_flags_orig = item['Tail flags']
                tail_flags = True if "true" in tail_flags_orig.lower() else False
                
                tail_twitches_orig = item['Tail twitches']
                tail_twitches = True if "true" in tail_twitches_orig.lower() else False
                
                approaches_orig = item['Approaches']
                approaches = True if "true" in approaches_orig.lower() else False
                
                indifferent_orig = item['Indifferent']
                indifferent = True if "true" in indifferent_orig.lower() else False
                
                runs_from_orig = item['Runs from']
                runs_from = True if "true" in runs_from_orig.lower() else False
            )
            s.save()





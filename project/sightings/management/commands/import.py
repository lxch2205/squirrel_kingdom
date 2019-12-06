import csv

from django.core.management.base import BaseCommand
from sightings.modela import Squirrel


class Command(BaseCommand):
    def add_arguments(self,parser):
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
                date = item['Date']
                age = item['Age']
                color = item['Primary Fur Color']
                location = item['Location']
                specific_location = item['Specific Location']
                running = item['Running']
                #running = True if "true" in running_1.lower() else False
                chasing = item['Chasing']
                #chasing = True if "true" in chasing_1.lower() else False
                climbing = item['Climbing']
                #climbing = True if "true" in climbing_1.lower() else False
                eating = item['Eating']
                #eating = True if "true" in eating_1.lower() else False
                foraging = item['Foraging']
                #foraging = True if "true" in foraging_1.lower() else False
                other_activities = item['Other Activities']
                kuks = item['Kuks']
                #kuks = True if "true" in kuks_1.lower() else False
                quaas = item['Quaas']
                #quaas = True if "tr'e" in quaas_1.lower() else False
                moans = item['Moans']
                #moans = True if "true" in moans_1.lower() else False
                tail_flags = item['Tail flags']
                #tail_flags = True if "true" in tail_flags_1.lower() else False
                tail_twitches = item['Tail twitches']
                #tail_twitches = True if "true" in tail_twitches_1.lower() else False
                approaches = item['Approaches']
                #approaches = True if "true" in approaches_1.lower() else False
                indifferent = item['Indifferent']
                #indifferent = True if "true" in indifferent_1.lower() else False
                runs_from = item['Runs from']
                #runs_from = True if "true" in runs_from_1.lower() else False
            )
            s.save()





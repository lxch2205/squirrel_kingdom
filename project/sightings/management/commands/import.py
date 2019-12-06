import csv

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('csv file')
    def handle(self, *args, **options):
        with open(options['csv file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        for item in data:
            s = Squirrel(
                latitude = item[0],
                longitude = item[1],
                id = item[2]
                shift = item[4]
                date = item[5]
                age = item[7]
                color = item[8]
                location = item[12]
                specific_location = item[14]
                running_1 = item[15]
                running = True if "true" in running_1.lower() else False
                chasing_1 = item[16]
                chasing = True if "true" in chasing_1.lower() else False
                climbing_1 = item[17]
                climbing = True if "true" in climbing_1.lower() else False
                eating_1 = item[18]
                eating = True if "true" in eating_1.lower() else False
                foraging_1 = item[19]
                foraging = True if "true" in foraging_1.lower() else False
                other_activities = item[20]
                kuks_1 = item[21]
                kuks = True if "true" in kuks_1.lower() else False
                quaas_1 = item[22]
                quaas = True if "true" in quaas_1.lower() else False
                moans_1 = item[23]
                moans = True if "true" in moans_1.lower() else False
                tail_flags_1 = item[24]
                tail_flags = True if "true" in tail_flags_1.lower() else False
                tail_twitches_1 = item[25]
                tail_twitches = True if "true" in tail_twitches_1.lower() else False
                approaches_1 = item[26]
                approaches = True if "true" in approaches_1.lower() else False
                indifferent_1 = item[27]
                indifferent = True if "true" in indifferent_1.lower() else False
                runs_from_1 = item[21]
                runs_from = True if "true" in runs_from_1.lower() else False
            )
            s.save()





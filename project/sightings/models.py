from django.db import models

from django.utils.translation import gettect as _

class Squirrel(models.Models):
    id = models.CharField(
        help_text=_('Unique Squirrel ID'),
        max_length=255,
        primary_key=True,
    )

    latitude = models.DecimalField(
        help_text=_('Latitude'),
        max_digits=25,
        decimal_places=20,
    )

    longitude = models.DecimalField(
        help_text=_('Longitude'),
        max_digits=25,
        decimal_places=20,
    )
    
    AM = 'AM'
    PM = 'PM' 

    SHIFT_CHOICES = (
        (AM,'AM'),
        (PM,'PM'),
    )

    shift = models.CharField(
        help_text=_('Shift'),
        max_length=16,
        choices=SHIFT_CHOICES,
        default=AM, # ?
    )




# Create your models here.

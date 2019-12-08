from django.shortcuts import render, redirect

from .models import Squirrel
from .forms import SquirrelForm

import random


def index(request):
    return render(request, 'sightings/index.html')

def all_squirrels(request):
    squirrel_ids = list()
    for i in Squirrel.objects.all():
        i_dict = {}
        i_dict['id'] = i.id
        squirrel_ids.append(i_dict)
    return render(request, 'sightings/list.html', {'squirrel_ids':squirrel_ids})

def squirrel_details(request, squirrel_id):
    data = Squirrel.objects.get(squirrel_id=squirrel_id)
    context = {
        'data': data
    }
    return render(request, 'sightings/detail.html', context)

def add_squirrel(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(f'/sightings/list/')
    return render(request, 'sightings/add.html')

def stats(request):
    dataset = Squirrel.objects \
        .values('shift') \
        .annotate(running_count=Count('shift', filter=Q(running=True)),
                not_running_count=Count('shift', filter=Q(running=False))) \
        .order_by('shift')
    return render(request, 'sightings/stats.html', {'dataset': datasest})

def map(request):
    sightings = random.sample(list(Squirrel.objects.all()),100)
    return render(request, 'map/map.html',{'sightings':sightings})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Squirrel
from .forms import SquirrelForm

import json
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

def add_squirrel(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(f'/sightings/list')
    else:
        form = SquirrelForm()
    context = {
        'form': form,
    }
    return render(request, 'sightings/add.html', context)

def squirrel_details(request, id):
    try:
        data = Squirrel.objects.get(id=id)
    except Squirrel.DoesNotExist:
        data = None
    context = {
        'data': data
    }
    return render(request, 'sightings/detail.html', context)

def map(request):
    sightings = random.sample(list(Squirrel.objects.all()), 100)
    return render(request, 'map/map.html', {'sightings':sightings})

def stats(request):
    gray_count = Squirrel.objects.filter(color='Gray').count(),
    cinnamon_count = Squirrel.objects.filter(color='Cinnamon').count(),
    black_count = Squirrel.objects.filter(color='Black').count(),
    adult_count = Squirrel.objects.filter(age='Adult').count(),
    juvenile_count = Squirrel.objects.filter(age='Juvenile').count(),
    above_ground_count = Squirrel.objects.filter(location='Above Ground').count(),
    ground_plane_count = Squirrel.objects.filter(location='Ground Plane').count(),
    approaches_count = Squirrel.objects.filter(approaches=True).count(),
    indifferent_count = Squirrel.objects.filter(indifferent=True).count(),
    runs_from_count = Squirrel.objects.filter(runs_from=True).count(),
    running_true_count = Squirrel.objects.filter(running=True).count(),
    chasing_true_count = Squirrel.objects.filter(chasing=True).count(), 
    climbing_true_count = Squirrel.objects.filter(climbing=True).count(),
    eating_true_count = Squirrel.objects.filter(eating=True).count(),
    foraging_true_count = Squirrel.objects.filter(foraging=True).count(),
    
    context ={
            'gray_count':gray_count, 
            'cinnamon_count':cinnamon_count, 
            'black_count':black_count, 
            'adult_count':adult_count, 
            'juvenile_count':juvenile_count, 
            'above_ground_count':above_ground_count, 
            'ground_plane_count':ground_plane_count, 
            'approaches_count':approaches_count, 
            'indifferent_count':indifferent_count, 
            'runs_from_count':runs_from_count, 
            'running_true_count':running_true_count, 
            'chasing_true_count':chasing_true_count, 
            'climbing_true_count':climbing_true_count, 
            'eating_true_count':eating_true_count, 
            'foraging_true_count':foraging_true_count,
        }
    context = json.dumps(context)

    return render(request, 'sightings/stats.html', locals())

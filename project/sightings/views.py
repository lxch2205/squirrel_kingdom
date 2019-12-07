from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.db.models import Count, Q

from .models import Squirrel
from .forms import SquirrelForm

def all_squirrels(request):
    squirrels = Squirrel.objects.all()
    field_names = Squirrel._meta.get_fields()
    context = {
        'squirrels' : squirrels.order_by('id'),
        'field_names': field_names
    }
    return render(request, 'sightings/all_squirrels.html', context)

def add_squirrel(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/lists/')
    else:
        form = SquirrelForm()

    context = {
        'form': form
    }

    return render(request, 'sightings/add.html', context)

def squirrel_details(request, squirrel_id):
    data = Squirrel.objects.get(squirrel_id=squirrel_id)
    context = {
        'data': data
    }
    return render(request, 'sightings/detail.html', context)

def stats(request):
    dataset = Squirrel.objects \
        .values('shift')\
        .annotate(


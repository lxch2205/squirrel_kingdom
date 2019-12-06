from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import UpdateView
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
        #check data with form
        if form.is_valid():
            x = form['id'].value()
            form.save()
            return redirect(f'/sightings/{x}')
    else:
        form = SquirrelForm()
        return render(request, 'sightings/add.html',{'form': form})


# Create your views here.

from django.shortcuts import render
from models import Squirrel
from django.http import HttpResponse

def catalog(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels' : squirrels.order_by('id'),
    }
    return render(request,'sightings/catalog.html',context)

def add_squirrel(request):
    if request.method == 'POST':
        form = 


# Create your views here.

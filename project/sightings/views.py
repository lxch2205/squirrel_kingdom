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
        form = SquirrelForm(request.POST)
        #check data with form
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/


# Create your views here.

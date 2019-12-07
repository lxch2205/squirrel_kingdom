from django.shortcuts import render, redirect

from .models import Squirrel
from .forms import SquirrelForm


def index(request):
    return render(request, 'sightings/index.html')

def all_squirrels(request):
    squirrel_list = Squirrel.objects.order_by('id')
    context = {
        'squirrels_list' : squirrel_list
    }
    return render(request, 'sightings/list.html', context)

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

def map(request):
    latlong = list()
    for i in Squirrel.objects.all():
        loc_dict = {}
        loc_dict['latitude']=i.latitude
        loc_dict['longtitude']=i.longitude
        latlong.append(loc_dict)
    return render(request, 'map/map.html', {'latlong':latlong})

def stats(request):

    total_squirrels = Squirrel.objects.count()
    gray = Squirrel.objects.filter(color='Gray').count()
    cinnamon = Squirrel.objects.filter(color='Cinnamon').count()
    black = Squirrel.objects.filter(color='Black').count()
    adult = Squirrel.objects.filter(age='Adult').count()
    juvenile = Squirrel.objects.filter(age='Juvenile').count()
    above_ground = Squirrel.objects.filter(location='Above Ground').count()
    ground_plane = Squirrel.objects.filter(location='Ground Plane').count()
    approaches = Squirrel.objects.filter(approaches='Approaches').count()
    indifferent = Squirrel.objects.filter(indifferent='Indifferent').count()
    runs_from = Squirrel.objects.filter(runs_from='Runs from').count()
    running_true = Squirrel.objects.filter(running=True).count()
    chasing_true = Squirrel.objects.filter(chasing=True).count()  
    climbing_true = Squirrel.objects.filter(climbing=True).count()
    eating_true = Squirrel.objects.filter(eating=True).count()
    foraging_true = Squirrel.objects.filter(foraging=True).count()
    #other_activities_true = Squirrel.objects.filter(other_activities=True).count()

    context = {
            'total_squirrels' : total_sightings,
            'gray' :gray,
            'cinnamon' : cinnamon
            'black' : black
            'adult' : adult
            'juvenile' : juvenile
            'above_ground' : above_ground
            'ground_plane' : ground_plane
            'approaches' : approaches
            'indifferent' : indifferent
            'runs_from' : run_from
            'running_true' : running
            'chasing_true' : chasing
            'climbing_true' : climbing
            'eating_true' : eating
            'foraging_true' : foraging
            }
    return render(request, 'sightings.status.html', context)



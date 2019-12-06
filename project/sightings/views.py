from django.shortcuts import render
from models import Squirrel
from django.http import HttpResponse

def catalog(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels' : squirrels.order_by('id'),
    }
    return render

# Create your views here.

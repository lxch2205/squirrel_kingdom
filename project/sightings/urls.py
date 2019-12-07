from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('sightings/', views.all_squirrels, name='sightings'),
    path('sightings/<str:squirrel_id>/', views.detial, name='detail'),
    path('sightings/add/', views.add_squirrel, name='add'),
    path('sightings/stats/', views.stats, name='stats'),
]

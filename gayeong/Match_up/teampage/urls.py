from django.contrib import admin
from django.urls import path, include 

from.import views

app_name = "teampage"

urlpatterns = [
    path('management/', views.management, name = 'management'),
    path('teaminfo/', views.teaminfo, name = "teaminfo"),
    path('testpage/', views.testpage, name = "testpage"),
    path('simulation/', views.simulation, name = "simulation"),
]

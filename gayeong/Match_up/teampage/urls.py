from django.contrib import admin
from django.urls import path, include 

from.import views

app_name = "teampage"

urlpatterns = [
    path('management/', views.management, name = 'management'),
    path('teaminfo/', views.teaminfo, name = "teaminfo"),
    path('testpage/', views.testpage, name = "testpage"),
    path('simulation/', views.simulation, name = "simulation"),
    path('team_list/', views.team_list, name = "team_list"),
    path('team_create/', views.team_create, name = "team_create"),
    path('teamdetail/<int:id>/', views.teamdetail, name = "teamdetail"),
    path('postcreate/', views.postcreate, name = "postcreate"),

    path('info_turnBack/', views.info_turnBack, name = "info_turnBack"),
]

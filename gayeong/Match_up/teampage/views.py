from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import auth
from account.models import *
from .models import *
from .forms import *
from account.forms import *

# Create your views here.
def teaminfo(request):
    error = ""
    try:
            
        my_profile = Profile.objects.get(user__username=request.user)
        teamname = my_profile.teams
        print(teamname.all().count())
        if teamname.all().count() == 0: 
            print("팀 없음")
        else:
            tes = my_profile.teams.all()
            print(tes)

        print(my_profile)
    except:
        error = "로그인하지 않았습니다."
        my_profile = ""
        tes = ""

    context = {
        "my_profile" : my_profile,
        "error" : error,
        "tes" : tes,
    }

    return render(request, 'teaminfo.html', context)

def management(request):
    return render(request, 'management.html')

def testpage(request):
    return render(reqeust, 'testpage.html')

def simulation(request):
    return render(request, 'simulation.html')

def team_list(request):
    team_list = Team.objects.all()
    context = {
        "team_list" : team_list
    }
    return render(request, 'team_list.html', context)

def team_create(request):
    if request.method == "POST":
        tform = TeamForm(request.POST)
        if tform.is_valid():
            creater = Profile.objects.get(user__username=request.user)
            
            team_form = tform.save(commit=False)
            team_form.king = creater
            team_form.personnel = team_form.personnel+1
            team_form.intro = request.POST.get("intro")
            team_form.phone = creater.phone
            team_form.save()
            
            named = Team.objects.get(team_name = team_form.team_name)
            creater.teams.add(named)
            creater.save() 
            
            return redirect('/teaminfo')

    else:
        team_list = Team.objects.all()
        tform = TeamForm()
        context = {
            "team_list" : team_list,
            "tform" : tform,
        }
        return render(request, 'team_create.html', context)

def info_turnBack(request):
    return redirect('/teaminfo')

def teamdetail(request, id):
    username = request.user.username
    us1 = Profile.objects.get(user__username=request.user)
    user_team = us1.teams
    tea = Team.objects.get(pk = id)

    context = {
        "tea":tea,
        "user_team": user_team,
    }
    
    return render(request, 'teamdetail.html', context)

def postcreate(reqeust):
    return render(request, 'teamcreate.html')
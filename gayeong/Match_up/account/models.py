
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

first_region = [
        ('경기', '경기도'),
        ('강원', '강원도'),
        ('경북', '경상북도'),
        ('경남', '경상남도'),
        ('충북', '충청북도'),
        ('충남', '충청남도'),
        ('전북', '전라북도'),
        ('전남', '전라남도'),
        ('제주', '제주도'),
    ]

class Team(models.Model):

    team_name = models.CharField(max_length = 15, unique = True)
    personnel = models.PositiveIntegerField(default = 0)
    team_image = models.ImageField(upload_to = 'team_image', blank = True)
    region = models.CharField(max_length = 7, choices=first_region)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.team_name


class Profile(models.Model):

    two_region = [
        ('선택없음', '시, 도를 먼저 선택해주세요')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length = 13, unique = True)
    email = models.EmailField(null=True, blank=False, unique=True)
    phone = models.CharField(max_length = 11, unique = True)
    f_region = models.CharField(max_length = 7, choices = first_region)
    w_region = models.CharField(max_length = 7, choices = two_region, default = "시, 도를 먼저 선택해주세요")
    age = models.PositiveIntegerField(null = True)

    teams = models.ManyToManyField(Team, help_text="원하는 팀은 선택하세요")

    def __str__(self):
        return self.user_name


    

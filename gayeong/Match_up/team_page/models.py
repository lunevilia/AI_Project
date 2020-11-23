from django.db import models
from django.conf import settings
from account.models import *
    



class TimeDate(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    class Meta:
        abstract = True


class Team():
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

    team_name = models.CharField(max_length = 15, unique = True)
    personnel = models.PositiveIntegerField()
    team_image = models.ImageField(upload_to = 'team_image', blank = True)
    region = models.CharField(max_length = 7, choices = first_region)
    phone = models.CharField(max_length=11)
 
#python manage.py makemigrations
from django.db import models
from django.conf import settings
from account.models import *
from community.models import *




class Game_Result(models.Model):
    winner = models.CharField(max_length = 15, null = True)
    coner = models.PositiveIntegerField(default = 0)
    penalty = models.PositiveIntegerField(default = 0)
    offside = models.PositiveIntegerField(default = 0)
    warn = models.PositiveIntegerField(default = 0)
    late = models.BooleanField(default = False )
    foul = models.PositiveIntegerField(default = 0)


class Game(models.Model):
    team_right = models.CharField(max_length=15)
    team_left = models.CharField(max_length=15)
    place = models.CharField(max_length = 25, null = True)
    date = models.DateTimeField(auto_now=True)
    finish = models.BooleanField(default = False)
    results = models.ForeignKey(Game_Result, on_delete = models.PROTECT)


#python manage.py makemigrations


class Team_Post(TimeDate):
    ZeroOrOne = [
        ('일반', '일반'),
        ('공지사항', '공지사항'),
    ]

    team_name = models.ForeignKey(Team, on_delete = models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE) # 작성자
    title = models.CharField(max_length=200)
    title_image = models.ImageField(upload_to = 'image', blank=True)
    content = models.TextField()
    importent = models.CharField(max_length=10, choices=ZeroOrOne)
    

    def __str__(self):
        return self.title

    #1번 글의 경우 -> post/1
    def get_absolute_urls(self):
        return reverse("team", args=[str(self.id)]).py

    def is_title_more11s(self):
        return len(self.title) > 11
    
    def get_title_under11s(self):
        return self.title[:11]
 
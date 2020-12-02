from django import forms
from .models import *
from django.forms.widgets import ClearableFileInput

class Team_Post_Form(forms.ModelForm):
    class Meta:
        model = Team_Post
        fields = ('title', 'title_image', 'content', 'importent')
        labels = {
            'title': '',
            'title_image': '',
            'content': '',
            'importent': '',
        }
        
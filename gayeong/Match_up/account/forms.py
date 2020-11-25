from django import forms
from .models import *
from django.forms.widgets import ClearableFileInput

class SignupForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user_name', 'email', 'phone', 'f_region')
        labels = {
            'user_name': '',
            'email': '',
            'phone': '',
            'f_region': '',
        }
        
class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('team_name', 'team_image','region')
        labels = {
            'team_name': '',
            'team_image': '',
            'region': '',
        }
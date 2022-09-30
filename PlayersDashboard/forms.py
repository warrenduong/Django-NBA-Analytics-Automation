from django import forms
from PlayersDashboard.models import PlayerStats


class PlayerQueryForm(forms.ModelForm):
    class Meta:
        model = PlayerStats
        fields = ['player', 'pos', ]

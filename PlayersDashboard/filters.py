import django_filters
from .models import PlayerStats
from django_filters import ModelChoiceFilter


class PlayerFilter(django_filters.FilterSet):

    class Meta:
        model = PlayerStats
        fields = ['player', 'pos', 'tm']

from django import forms
from .models import PlayerStat


class PlayerStatForm(forms.ModelForm):
    class Meta:
        model = PlayerStat
        fields = [
            'player_name',
            'team',
            'opponent',
            'game_date',
            'points',
            'rebounds',
            'assists',
        ]

        widgets = {
            'game_date': forms.DateInput(attrs={'type': 'date'}),
        }
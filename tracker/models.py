from django.db import models

from django.db import models


class PlayerStat(models.Model):
    player_name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    opponent = models.CharField(max_length=100)
    game_date = models.DateField()
    points = models.IntegerField(default=0)
    rebounds = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)

    def __str__(self):
        return self.player_name
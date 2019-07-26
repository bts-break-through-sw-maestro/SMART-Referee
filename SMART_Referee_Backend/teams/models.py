from django.db import models

class Teams(models.Model):
    team_name = models.CharField(max_length=40, blank=False)
    line_up = models.CharField(max_length=200, blank=True)
    players = models.CharField(max_length=400, blank=False)
    
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    
    region = models.CharField(max_length=60)

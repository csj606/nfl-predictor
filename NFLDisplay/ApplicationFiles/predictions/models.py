from django.db import models

# Create your models here.


class Weather(models.TextChoices):
    CLEAR = "c",
    LIGHT_RAIN = "lr",
    HEAVY_RAIN = "hr",
    LIGHT_SNOW = "ls",
    HEAVY_SNOW = "hs"


class Team(models.Model):
    name = models.CharField


class GameWeek(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()


class Game(models.Model):
    start_time = models.DateTimeField()
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    weather = models.CharField(choices=Weather)




from django.db import models

# Create your models here.

class BandCharacter(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    player_one_opinion = models.CharField(max_length=1500)
    player_two_opinion = models.CharField(max_length=1500)
    player_three_opinion = models.CharField(max_length=1500)
    player_four_opinion = models.CharField(max_length=1500)
    player_five_opinion = models.CharField(max_length=1500)
    player_six_opinion = models.CharField(max_length=1500)
    player_seven_opinion = models.CharField(max_length=1500)
    player_eight_opinion = models.CharField(max_length=1500)
    player_nine_opinion = models.CharField(max_length=1500)
    deceased_opinion = models.CharField(max_length=1500)
    goals = models.CharField(max_length=1500)
    clue1 = models.CharField(max_length=1500)
    clue2 = models.CharField(max_length=1500)
    clue3 = models.CharField(max_length=1500)
    clue4 = models.CharField(max_length=1500)
    clue5 = models.CharField(max_length=1500)

    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name
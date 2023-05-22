from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    player1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player1_games')
    player2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player2_games')
    status = models.CharField(max_length=20, default='pending')

class Move(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    x = models.IntegerField()
    y = models.IntegerField()

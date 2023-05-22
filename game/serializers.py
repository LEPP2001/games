from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Game, Move

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class GameSerializer(serializers.ModelSerializer):
    player1 = UserSerializer()
    player2 = UserSerializer()

    class Meta:
        model = Game
        fields = ('id', 'player1', 'player2', 'status')

class MoveSerializer(serializers.ModelSerializer):
    player = UserSerializer()

    class Meta:
        model = Move
        fields = ('id', 'game', 'player', 'x', 'y')
 
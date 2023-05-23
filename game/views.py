from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Game, Move
from .serializers import UserSerializer, GameSerializer, MoveSerializer
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
import requests

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class MoveViewSet(viewsets.ModelViewSet):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer

# Renderizar la base
@login_required
def base(request):
    return render(request, 'base.html')

# Renderizar la vista del perfil
@login_required
def profile(request):
    return render(request, 'profile.html')

# Renderizar los juegos
@login_required
def games(request):
    return render(request, 'games.html')

# Renderizar el aboutme
@login_required
def about(request):
    return render(request, 'about.html')

# Renderizar la salida
@login_required
def exit(request):
    logout(request)
    return redirect(base)

# Renderizar html con el juego gato
@login_required
def gato(request):
    url = 'https://juegosgamesx.blob.core.windows.net/gato/gato.html'
    response = requests.get(url)
    content = response.content.decode('utf-8')
    return render(request, 'games/gato/gato.html', {'content': content})

# Renderizar html con las instrucciones del gato
@login_required
def gatoInst(request):
    url = 'https://juegosgamesx.blob.core.windows.net/gato/instruccionesGato.html'
    response = requests.get(url)
    content = response.content.decode('utf-8')
    return render(request, 'games/gato/gatoInst.html', {'content': content})

# Renderizar html con el juego T. Hanoi
@login_required
def hanoi(request):
    url = 'https://juegosgamesx.blob.core.windows.net/torres-hanoi/torresHanoi.html'
    response = requests.get(url)
    content = response.content.decode('utf-8')
    return render(request, 'games/hanoi/hanoi.html', {'content': content})

# Renderizar html con las instrucciones de las T. Hanoi
@login_required
def hanoiInst(request):
    url = 'https://juegosgamesx.blob.core.windows.net/torres-hanoi/instruccionesHanoi.html'
    response = requests.get(url)
    content = response.content.decode('utf-8')
    return render(request, 'games/hanoi/hanoiInst.html', {'content': content})

# Renderizar el registro de usuario
def register(request):
    data = {
        'form' : CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            return redirect(base)
    return render(request, 'registration/register.html', data)

from django.urls import path
from game import views

urlpatterns = [
    path('', views.base, name='base'),  # la vista principal
    path('profile/', views.profile, name='profile'),  # la vista del perfil
    path('games/', views.games, name='games'),  # la vista games
    path('logout/', views.exit, name='exit'),  # la vista salir
    path('about/us/', views.about, name='about'),  # la vista about/us
    path('register/', views.register, name='register'),  # la vista de registro
    path('gato/', views.gato, name='gato'),  # la vista del gato
    path('gato/instrucciones/', views.gatoInst, name='gatoInst'),  # la vista de inst. gato
    path('hanoi/', views.hanoi, name='hanoi'),  # la vista del hanoi
    path('hanoi/instrucciones/', views.hanoiInst, name='hanoiInst'),  # la vista de inst. hanoi
]

# alumnos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('menú/', views.index, name='index'),
    path('compra/', views.compra, name='compra'),
    path('envivo/', views.envivo, name='envivo'),
    path('información/', views.info, name='info'),
    path('reseña/', views.resena, name='resena'),
    path('registro/', views.login, name='login'),
    path('registro/index.html', views.index, name='volverLogin'),
    path('registro/login.html', views.login, name='iniciosesion'),
    
    
]

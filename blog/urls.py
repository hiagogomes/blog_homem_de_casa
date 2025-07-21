from django.urls import path 
from . import views  

urlpatterns = [
    path('', views.home, name='home'),  
    path('sobre/', views.sobre, name='sobre'),
    path('politica_privacidade/', views.politica_privacidade, name='politica_privacidade'),
    path('politica_afiliado/', views.politica_afiliado, name='politica_afiliado'),
    path('termos_uso/', views.termos_uso, name='termos_uso'),
    path('contato/', views.contato, name='contato'),
    path('playstation/', views.playstation, name='playstation'),
    path('relogios/', views.relogios, name='relogios'),
    path('parafusadeira/', views.parafusadeira, name='parafusadeira'),
    path('panelas/', views.panelas, name='panelas'),
    path('airfryer/', views.airfryer, name='airfryer'),
    path('fones/', views.fones, name='fones'),
    path('echopop/', views.echopop, name='echopop'),
    path('lavadora/', views.lavadora, name='lavadora'),
    path('jogo/', views.jogo, name='jogo'),
]
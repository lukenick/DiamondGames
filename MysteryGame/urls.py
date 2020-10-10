from django.urls import path

from . import views

app_name = 'MysteryGame'
urlpatterns = [
    path('', views.index, name='index'),
    path('join', views.join, name='join'),
    path('host', views.host, name='host'),
    path('info', views.info, name='info'),
    path('band', views.band, name='band'),
    path('reveal', views.reveal, name='reveal'),
    path('join?input_code=<str:character_id>', views.character, name='character'),
    path('character/<str:character_id>-<str:clue_id>', views.character_with_clues, name='character_with_clues'),
    path('character/<str:character_id>', views.character, name='character'),
]

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import BandCharacter

def index(request):
    return render(request, 'MysteryGame/index.html')

def join(request):
    return render(request, 'MysteryGame/join.html')

def host(request):
    return render(request, 'MysteryGame/host.html')

def band(request):
    global_character = BandCharacter.objects.get(pk=10)
    all_characters = BandCharacter.objects.order_by('pk')
    return render(request, 'MysteryGame/band.html', {'global_character': global_character, 'all_characters': all_characters})



def character(request, character_id):
    this_character = BandCharacter.objects.get(code=character_id)
    global_character = BandCharacter.objects.get(pk=10)
    all_characters = BandCharacter.objects.order_by('pk')
    return render(request, 'MysteryGame/character.html', {'this_character': this_character, 'global_character': global_character, 'all_characters': all_characters})

def character_with_clues(request, character_id, clue_id):
    this_character = BandCharacter.objects.get(code=character_id)
    global_character = BandCharacter.objects.get(pk=10)
    all_characters = BandCharacter.objects.order_by('pk')
    return render(request, 'MysteryGame/character.html', {'this_character': this_character, 'global_character': global_character, 'all_characters': all_characters, 'clue_id': clue_id})
from django.shortcuts import render
from .models import Character


def character_list(request):
    characters = Character.objects.order_by('equipe')
    return render(request, 'pilote/character_list.html', {'characters' : characters})
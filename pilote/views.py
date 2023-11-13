from django.shortcuts import render
from .models import Character


def character_list(request):
    pilotes = Character.objects
    return render(request, 'pilote/character_list.html', {})
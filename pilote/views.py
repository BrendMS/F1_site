from django.shortcuts import render, get_object_or_404 , redirect
from .models import Character, Equipement
from pilote.forms  import MoveForm


def character_list(request):
    characters = Character.objects.order_by('equipe')
    equipements = Equipement.objects.order_by('disponibilite')
    return render(request, 'pilote/character_list.html', {'characters' : characters, 'equipements': equipements})

def character_detail(request, id_character):
    character = get_object_or_404(Character, id_character=id_character)
    form=MoveForm()
    if form.is_valid():
        ancien_lieu = get_object_or_404(Equipement, id_equip=character.lieu.id_equip)
        ancien_lieu.disponibilite = "libre"
        ancien_lieu.save()
        form.save()
        nouveau_lieu = get_object_or_404(Equipement, id_equip=character.lieu.id_equip)
        nouveau_lieu.disponibilite = "occupé"
        nouveau_lieu.save()
        return redirect('character_detail', id_character=id_character)
    else:
        form = MoveForm()
        return render(request,
                  'pilote/character_detail.html',
                  {'character': character, 'lieu': character.lieu, 'form': form})
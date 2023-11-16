from django.shortcuts import render, get_object_or_404 , redirect
from .models import Character, Equipement
from pilote.forms  import MoveForm


def character_list(request):
    characters = Character.objects.order_by('equipe')
    equipements = Equipement.objects.order_by('disponibilite')
    return render(request, 'pilote/character_list.html', {'characters' : characters, 'equipements': equipements})

def change_ok(etat, nouveau_lieu):
    ok = True

    if etat == 'fatigué' and nouveau_lieu == 'pit':
        ok = False
    
    elif etat == 'pas préparé' and nouveau_lieu == 'piste de course':
        ok = False

    return ok

def changement_etat(lieu):
    if lieu == 'pit':
        etat = "gymnasium"

    elif lieu == 'gymnasium':
        etat = "Fatigué"

        
    return etat

def character_detail(request, id_character):
    character = get_object_or_404(Character, id_character=id_character)
    ancien_lieu = get_object_or_404(Equipement, id_equip=character.lieu.id_equip)

    form = MoveForm(request.POST, instance=character)

    error = None
    message = ""

    if form.is_valid() and request.method == "POST":
        form.save(commit=False)
        nouveau_lieu = get_object_or_404(Equipement, id_equip=character.lieu.id_equip)

        if change_ok(character.etat, nouveau_lieu.id_equip):
            print("oi")
            if nouveau_lieu.disponibilite == "libre":

                if nouveau_lieu.id_equip == "piste de course":
                    occupants = []
                    pilotes = Character.objects.all().order_by('id_character')
                    for pilote in pilotes:
                        if character_x.lieu.id_equip == "piste de course":
                            occupants.append(pilote.id_character)
                    if len(occupants) == 2:
                        nouveau_lieu.disponibilite = "occupé"
                    else:
                            nouveau_lieu.disponibilite = "libre"
                
                nouveau_lieu.save()
                character.lieu = nouveau_lieu
                #character.etat = change_ok(character.lieu.id_equip)
                character.save()
                message = f"{character.id_character} est dans le lieu démandé ({nouveau_lieu.id_equip})"
                form.save()
                return redirect('character_detail', id_character=id_character)

            else:
                error = True
                occupants = []
                pilotes = Character.objects.all().order_by('id_character')
                for pilote in pilotes:
                    if pilote.lieu.id_equip == nouveau_lieu.id_equip:
                        occupants.append(pilote.id_character)
                message = f"{nouveau_lieu.id_equip} est deja occupé(e) par {','.join(occupants)}"
        else:
            error = True
            message = f"{character.id_character} ne peut pas aller au lieu demandé ({nouveau_lieu.id_equip}) dans son état actuel ({character.etat})"
        return render(request,
            'pilote/character_detail.html',
            {'character': character, 'message': message, 'error': error, 'lieu': ancien_lieu, 'nouveau_lieu': nouveau_lieu, 'form': form})
    else:
        form = MoveForm()
        return render(request,
            'pilote/character_detail.html',
            {'character': character, 'lieu': ancien_lieu, 'form': form})
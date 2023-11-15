from django import forms
 
from pilote.models import Character, Equipement
 
class MoveForm(forms.ModelForm):
 
    class Meta:
        model = Character
        fields = ('equipe', 'etat', 'lieu', 'photo')

        model_equip = Equipement
        fields_equip = ('disponibilite', 'photo') 


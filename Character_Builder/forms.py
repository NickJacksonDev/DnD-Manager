from django import forms
from .models import Character, AbilityScoreSet, AbilityScore

class CreateCharacterForm(forms.ModelForm):
	class Meta:
		model = Character
		fields = [
			'characterName', 
			'level', 
			'xp', 
			'maxHP', 
			'currentHP', 
			'alignment', 
			'size',
			'public'
		]

#Don't use this
class EditCharacterForm(forms.ModelForm):
	class Meta:
		model = Character
		fields = [
			'characterName', 
			'level', 
			'xp', 
			'maxHP', 
			'currentHP', 
			'alignment'
		]

class EditAbilityScoresForm(forms.ModelForm):
	class Meta:
		model = AbilityScoreSet
		fields = [
			'character',
			'strength',
			'dexterity',
			'constitution',
			'intelligence',
			'wisdom',
			'charisma'
		]
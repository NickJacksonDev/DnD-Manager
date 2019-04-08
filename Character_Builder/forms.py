from django import forms
from .models import Character, AbilityScoreSet, AbilityScore

class CreateCharacterForm(forms.ModelForm):
	class Meta:
		model = Character
		fields = [
			'public',
			'characterName', 
			'level', 
			'xp', 
			'maxHP', 
			'currentHP', 
			'alignment', 
			'size',
			'strength',
			'dexterity',
			'constitution',
			'intelligence',
			'wisdom',
			'charisma'
		]

# Now unused to prevent needing to access another from within a form.
class EditAbilityScoresForm(forms.ModelForm):
	class Meta:
		model = AbilityScoreSet
		fields = [
			# 'character',
			'strength',
			'dexterity',
			'constitution',
			'intelligence',
			'wisdom',
			'charisma'
		]
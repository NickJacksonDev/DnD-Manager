from django.test import TestCase
from .models import *

# Test Constants
DEFAULT_LEVEL = 0
DEFAULT_XP = 0
DEFAULT_HP = 6

class CharacterCreateTestCase(TestCase):
	def setUp(self):
		Character.objects.create(characterName="Malikar", alignment="Lawful Evil", size="Medium")

	def test_character_id(self):
		char = Character.objects.get(characterName="Malikar")
		self.assertEqual(char.characterID, 1)

	def test_character_name(self):
		try:
			Character.objects.get(characterName="Malikar")
		except:
			self.fail()

	def test_character_level(self):
		char = Character.objects.get(characterName="Malikar")
		self.assertEqual(char.level, DEFAULT_LEVEL)

	def test_character_xp(self):
		char = Character.objects.get(characterName="Malikar")
		self.assertEqual(char.xp, DEFAULT_XP)

	def test_character_max_hp(self):
		char = Character.objects.get(characterName="Malikar")
		self.assertEqual(char.maxHP, DEFAULT_HP)

	def test_character_current_hp(self):
		char = Character.objects.get(characterName="Malikar")
		self.assertEqual(char.currentHP, DEFAULT_HP)

	def test_character_alignment(self):
		char = Character.objects.get(characterName="Malikar")
		self.assertEqual(char.alignment, "Lawful Evil")

	def test_character_size(self):
		char = Character.objects.get(characterName="Malikar")
		self.assertEqual(char.size, "Medium")
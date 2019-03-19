from django.test import TestCase
from .models import *
from Character_Builder.models import *

class ItemCreateTestCase(TestCase):
	def setUp(self):
		Character.objects.create(characterName="Malikar", alignment="Lawful Evil", size="Medium")
		char = Character.objects.get(characterName="Malikar")
		Inventory.objects.create(character=char)
		inv = Inventory.objects.get(character=char)
		Item.objects.create(itemName="test item", inventory=inv)

	def test_inventory_id(self):
		char = Character.objects.get(characterName="Malikar")
		inv = Inventory.objects.get(character=char)
		self.assertEqual(inv.inventoryID, 1)

	def test_inventory_character(self):
		char = Character.objects.get(characterName="Malikar")
		inv = Inventory.objects.get(character=char)
		self.assertEqual(inv.character, char)

	def test_item_id(self):
		item = Item.objects.get(itemName="test item")
		self.assertEqual(item.itemID, 1)

	def test_item_name(self):
		item = Item.objects.get(itemName="test item")
		self.assertEqual(item.itemName, "test item")

	def test_item_inventory(self):
		char = Character.objects.get(characterName="Malikar")
		inv = Inventory.objects.get(character=char)
		item = Item.objects.get(itemName="test item")
		self.assertEqual(item.inventory, inv)

	def test_item_public(self):
		item = Item.objects.get(itemName="test item")
		self.assertEqual(item.public, True)		
from django.test import TestCase
from .models import *
from Character_Builder.models import *

# Campaign test cases
class CampaignCreateTestCase(TestCase):
    def setUp(self):
        Campaign.objects.create(campaignName="The Mountain")

    def test_campaign_name(self):
        try:
            Campaign.objects.get(campaignName="The Mountain")
        except:
            self.fail()

    def test_campaign_id(self):
        campaign = Campaign.objects.get(campaignName="The Mountain")
        self.assertEqual(campaign.campaignID, 1)

# CampaignDM test cases
class CampaignDMCreateTestCase(TestCase):
    def setUp(self):
        Campaign.objects.create(campaignName="The Mountain")
        Character.objects.create(characterName="Malikar", alignment="Lawful Evil", size="Medium")
        camp = Campaign.objects.get(campaignName="The Mountain")
        char = Character.objects.get(characterName="Malikar")
        CampaignDM.objects.create(character=char, campaign=camp)

    def test_campaign_dm_character(self):
        char = Character.objects.get(characterName="Malikar")
        try:
            CampaignDM.objects.get(character=char)
        except:
            self.fail()

    def test_campaign_dm_id(self):
        char = Character.objects.get(characterName="Malikar")
        dm = CampaignDM.objects.get(character=char)
        self.assertEqual(dm.campaignDMID, 1)

    def test_campaign_dm_campaign(self):
        char = Character.objects.get(characterName="Malikar")
        camp = Campaign.objects.get(campaignName="The Mountain")
        dm = CampaignDM.objects.get(character=char)
        self.assertEqual(dm.campaign, camp)

class PartyCreateTestCase(TestCase):
    def setUp(self):
        Campaign.objects.create(campaignName="The Mountain")
        camp = Campaign.objects.get(campaignName="The Mountain")
        Party.objects.create(campaign=camp)

    def test_party_id(self):
        camp = Campaign.objects.get(campaignName="The Mountain")
        party = Party.objects.get(campaign=camp)
        self.assertEqual(party.partyID, 1)

    def test_party_campaign(self):
        camp = Campaign.objects.get(campaignName="The Mountain")
        try:
            Party.objects.get(campaign=camp)
        except:
            self.fail()

class PartyCharacterCreateTestCase(TestCase):
    def setUp(self):
        Campaign.objects.create(campaignName="The Mountain")
        Character.objects.create(characterName="Malikar", alignment="Lawful Evil", size="Medium")
        camp = Campaign.objects.get(campaignName="The Mountain")
        char = Character.objects.get(characterName="Malikar")
        Party.objects.create(campaign=camp)
        par = Party.objects.get(campaign=camp)
        PartyCharacter.objects.create(character=char, party=par)

    def test_party_character_party(self):
        camp = Campaign.objects.get(campaignName="The Mountain")
        par = Party.objects.get(campaign=camp)
        pc = PartyCharacter.objects.get(party=par)
        self.assertEqual(pc.party, par)

    def test_party_character_character(self):
        camp = Campaign.objects.get(campaignName="The Mountain")
        par = Party.objects.get(campaign=camp)
        char = Character.objects.get(characterName="Malikar")
        try:
            PartyCharacter.objects.get(character=char)
        except:
            self.fail()

        
        
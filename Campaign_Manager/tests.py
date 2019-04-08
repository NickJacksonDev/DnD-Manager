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
        camp = Campaign.objects.get(campaignName="The Mountain")
        CampaignDM.objects.create(campaign=camp)

    def test_campaign_dm_id(self):
        camp = Campaign.objects.get(campaignName="The Mountain")
        dm = CampaignDM.objects.get(campaign=camp)
        self.assertEqual(dm.campaignDMID, 1)

    def test_campaign_dm_campaign(self):
        camp = Campaign.objects.get(campaignName="The Mountain")
        try:
            dm = CampaignDM.objects.get(campaign=camp)
        except:
            self.fail()

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

        
        
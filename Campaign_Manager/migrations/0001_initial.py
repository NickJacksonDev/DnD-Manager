# Generated by Django 2.1.7 on 2019-04-05 20:22

import Campaign_Manager.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Character_Builder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('campaignID', models.AutoField(primary_key=True, serialize=False)),
                ('campaignName', models.CharField(max_length=255)),
                ('image', models.ImageField(default='default_campaign.jpg', upload_to='campaign_pics')),
                ('creator', models.ForeignKey(default=Campaign_Manager.models.defaultUser, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CampaignDM',
            fields=[
                ('campaignDMID', models.AutoField(primary_key=True, serialize=False)),
                ('campaign', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Campaign_Manager.Campaign')),
                ('character', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Character_Builder.Character')),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('partyID', models.AutoField(primary_key=True, serialize=False)),
                ('campaign', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Campaign_Manager.Campaign')),
            ],
        ),
        migrations.CreateModel(
            name='PartyCharacter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Character_Builder.Character')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Campaign_Manager.Party')),
            ],
        ),
    ]

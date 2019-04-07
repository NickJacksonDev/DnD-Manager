# Generated by Django 2.1.7 on 2019-04-07 22:39

import Campaign_Manager.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Character_Builder', '0002_auto_20190407_1839'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('campaignID', models.AutoField(primary_key=True, serialize=False)),
                ('campaignName', models.CharField(max_length=255)),
                ('creator', models.ForeignKey(default=Campaign_Manager.models.defaultUser, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CampaignComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(null=True, upload_to='comment_pics')),
                ('slug', models.SlugField(default='default-slug')),
                ('author', models.ForeignKey(default=Campaign_Manager.models.defaultUser, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Campaign_Manager.Campaign')),
            ],
        ),
        migrations.CreateModel(
            name='CampaignDM',
            fields=[
                ('campaignDMID', models.AutoField(primary_key=True, serialize=False)),
                ('campaign', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Campaign_Manager.Campaign')),
                ('user', models.OneToOneField(default=Campaign_Manager.models.defaultUser, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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

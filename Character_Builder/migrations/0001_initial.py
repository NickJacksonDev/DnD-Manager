# Generated by Django 2.1.7 on 2019-03-10 15:46

import Character_Builder.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AbilityScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abilityName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AbilityScoreSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abilityScoreValue', models.IntegerField()),
                ('abilityScores', models.ManyToManyField(to='Character_Builder.AbilityScore')),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('characterID', models.IntegerField(default=Character_Builder.models.newCharacterID, unique=True)),
                ('characterName', models.CharField(max_length=255)),
                ('abilityScoreSetID', models.IntegerField(default=Character_Builder.models.newAbilityScoreSetID, unique=True)),
                ('level', models.IntegerField(default=0)),
                ('xp', models.IntegerField(default=0)),
                ('maxHP', models.IntegerField(default=6)),
                ('currentHP', models.IntegerField(default=6)),
                ('alignment', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CharacterClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('className', models.CharField(max_length=255)),
                ('hitDice', models.CharField(max_length=255)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Character_Builder.Character')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterRace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raceName', models.CharField(max_length=255)),
                ('abilityScoreBonusSetID', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('size', models.CharField(max_length=255)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Character_Builder.Character')),
            ],
        ),
        migrations.AddField(
            model_name='abilityscoreset',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Character_Builder.Character'),
        ),
    ]
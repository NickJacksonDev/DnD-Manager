# Generated by Django 2.1.7 on 2019-04-08 02:08

import Character_Builder.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Character_Builder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='race',
            field=models.ForeignKey(blank=True, default=Character_Builder.models.defaultRace, null=True, on_delete=django.db.models.deletion.PROTECT, to='Character_Builder.CharacterRace'),
        ),
    ]

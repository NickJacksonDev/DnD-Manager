# Generated by Django 2.1.7 on 2019-03-19 04:10

import Character_Builder.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Character_Builder', '0002_auto_20190318_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='user',
            field=models.ForeignKey(blank=True, default=Character_Builder.models.defaultUser, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-01 20:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0020_remove_forum_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quest', to=settings.AUTH_USER_MODEL),
        ),
    ]

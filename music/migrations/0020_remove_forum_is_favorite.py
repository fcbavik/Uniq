# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-01 20:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0019_remove_forum_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='is_favorite',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-31 07:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0033_remove_forum_artist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forum',
            old_name='album_title',
            new_name='name',
        ),
    ]

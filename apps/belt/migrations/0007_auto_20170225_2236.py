# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 06:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('belt', '0006_auto_20170225_2043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='book_id',
            new_name='book',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='user_id',
            new_name='user',
        ),
    ]

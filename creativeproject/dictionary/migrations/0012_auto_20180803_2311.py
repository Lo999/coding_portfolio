# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-03 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0011_auto_20180803_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='part_of_speech',
            field=models.CharField(choices=[('Verb', 'V'), ('Noun', 'N'), ('Particle', 'P'), ('Pronoun', 'PN'), ('Adjective', 'ADJ'), ('Adverb', 'ADV'), ('Preposition', 'PRE'), ('Interjection', 'I')], max_length=3),
        ),
    ]
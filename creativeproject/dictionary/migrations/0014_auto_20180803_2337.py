# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-03 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0013_auto_20180803_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='dialect',
            field=models.CharField(choices=[('Levantine', 'Levantine'), ('Egyptian', 'Egyptian'), ('Gulf', 'Gulf')], max_length=15),
        ),
        migrations.AlterField(
            model_name='entry',
            name='part_of_speech',
            field=models.CharField(choices=[('V', 'Verb'), ('N', 'Noun'), ('P', 'Particle'), ('PN', 'Pronoun'), ('ADJ', 'Adjective'), ('ADV', 'Adverb'), ('PRE', 'Preposition'), ('I', 'Interjection')], max_length=15),
        ),
    ]
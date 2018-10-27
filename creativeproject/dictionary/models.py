"""
Dictionary Models
"""

from enum import Enum

from django.db import models
from django.contrib.auth.models import *
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

import dictionary
from dictionary import validators as dictionary_validators

# Enums

class ChoiceEnum(Enum):
    """
    Defines choices for enums
    This is really stupid, unfortunately :/
    """
    @classmethod
    def choices(cls):
        return tuple((x.name, x.value) for x in cls)

class PartsOfSpeech(ChoiceEnum):
    Verb = "Verb"
    Noun = "Noun"
    Particle = "Particle"
    Pronoun = "Pronoun"
    Adjective = "Adjective"
    Adverb = "Adverb"
    Preposition = "Preposition"
    Interjection = "Interjection"

class Dialects(ChoiceEnum):
    Levantine = "Levantine"
    Egyptian = "Egyptian"
    Gulf = "Gulf"

# Main Models

class Language(models.Model):
    """
    Language Model
    Possible fields to come: location, script, characteristics, dialect...
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Entry(models.Model):
    """
    Entry Model
    """
    author = models.CharField(max_length=30) #make foreign key
    script_word = models.CharField(
            max_length=20,
            validators=[dictionary_validators.validate_arabic])
    arabizi_word = models.CharField(
            max_length=20,
            validators=[dictionary_validators.validate_not_arabic])
    part_of_speech = models.CharField(
            max_length=15,
            choices=PartsOfSpeech.choices())
    definition = models.CharField(
            max_length=150,
            validators=[dictionary_validators.validate_not_arabic])
    dialect = models.CharField(
            max_length=15,
            choices=Dialects.choices())

    def __str__(self):
        return "%s, %s, %s" % (
                self.script_word,
                self.arabizi_word,
                self.definition)

    def exists(self):
        """
        Returns true iff there exists an entry in the database having:
            (1) the same dialect AND the same part_of_speech
            (2) the same script_word OR the same arabizi_word
        """
        entries = Entry.objects.filter(
                dialect=self.dialect,
                part_of_speech=self.part_of_speech)
        return (
                entries.filter(script_word=self.script_word)
                or entries.filter(arabizi_word=self.arabizi_word))

    def validate_unique(self, exclude=None):
        """
        Override of Django's validate_unique cleaning method.
        Uses "exists" method to redefine the uniqueness of an entry.
        """
        if self.exists():
            raise ValidationError(
                _('The entry: (%(entry)s) already exists in Database'),
                params=dict(entry=self),
            )

    def save(self, *args, **kwargs):
        """
        Override of Django's save method to insert an instance into the DB.
        Calls "full_clean" to verify for uniqueness before insertion.
        """
        self.full_clean()
        super(Entry, self).save(*args, **kwargs)

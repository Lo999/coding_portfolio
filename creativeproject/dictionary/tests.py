"""
Dictionary Tests
good tutorial: http://test-driven-django-development.readthedocs.io/en/latest/02-models.html
"""
import django
from django.db import models as django_models
from django.contrib import auth
from django.test import TestCase
from django.core.exceptions import ValidationError


import dictionary
from dictionary.models import *

import accounts
from accounts.models import *

#Test Models
class EntryTestCase(TestCase):
    """
    Test class to test Entry Model
        sources:
        - https://goodcode.io/articles/django-assert-raises-validationerror/
    """
    def setUp(self):
        self.testuser1 = User.objects.create(
                username='testuser1',
                password='1z2x3c4v')
        self.entry1 = Entry.objects.create(
                author=self.testuser1,
                script_word='مرحبة',
                arabizi_word='mar7aba',
                part_of_speech=PartsOfSpeech.Interjection.value,
                definition='Hello',
                dialect=Dialects.Levantine.value)
        self.entry1_copy = Entry(
                author=self.testuser1,
                script_word='مرحبة',
                arabizi_word='mar7aba',
                part_of_speech=PartsOfSpeech.Interjection.value,
                definition='Hello',
                dialect=Dialects.Levantine.value)
        self.entry2 = Entry(
                author=self.testuser1,
                script_word='قطة',
                arabizi_word='2aTTa',
                part_of_speech=PartsOfSpeech.Noun.value,
                definition='Cat',
                dialect=Dialects.Levantine.value)

    def test_entry_script_word_must_contain_arabic(self):
        """
        Tests the validator "validate_arabic" works and validates the field
        "script_word" on the Entry model
        """
        self.entry2.script_word = 'not_arabic'
        with self.assertRaises(ValidationError):
            self.entry2.full_clean()

    def test_entry_arabizi_word_cannot_contain_arabic(self):
        """
        Tests the validator "validate_not_arabic" works and validates the field
        "arabizi_word" on the Entry model
        """
        self.entry2.arabizi_word = 'عربي'
        with self.assertRaises(ValidationError):
            self.entry2.full_clean()

    def test_entry_definition_cannot_contain_arabic(self):
        """
        Tests the validator "validate_not_arabic" works and validates the field
        "definition" on the Entry model
        """
        self.entry2.definition = 'عربي'
        with self.assertRaises(ValidationError):
            self.entry2.full_clean()

    def test_entry_exists_method_with_one_saved_entry(self):
        """
        Tests that the "entry(self)" method returns true for an entry that
        exists in the database
        """
        self.assertTrue(self.entry1.exists())

    def test_entry_exists_method_with_one_unsaved_entry(self):
        """
        Tests that the "entry(self)" method returns false for an entry that
        does not exist in the database AND is not equivalent to any entry
        in the database
        """
        self.assertFalse(self.entry2.exists())


    def test_entry_exists_method_with_two_entries(self):
        """
        Tests that the "entry(self)" method returns true for an entry that
        does not exist in the database BUT that is equivalent to some entry
        in the database
        """
        self.assertTrue(self.entry1_copy.exists())

    def test_entry_clean_validate_unique_checks_for_existence(self):
        """
        Tests that the "validate_unique" method raises the proper validation
        error if an unsaved model is equivalent to some entry in the database
        """
        try:
            self.entry1_copy.validate_unique()
            raise AssertionError("ValidationError not raised")
        except ValidationError as e:
            print(e)
            self.assertTrue(True)

    def test_entry_save_method_checks_for_existence(self):
        """
        Tests that the "save" method raises the proper validation error if
        an unsaved model is equivalent to some entry in the database. The
        current implementation accomplishes this by calling the "full_clean",
        which calls a custom "validate_unique" method, before calling super.
        """
        try:
            self.entry1_copy.save()
            raise AssertionError("ValidationError not raised")
        except ValidationError as e:
            print(e)
            self.assertTrue(True)




#Test Forms

#Test Views

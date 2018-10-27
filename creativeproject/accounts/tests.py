"""
Accounts Tests
good tutorial: http://test-driven-django-development.readthedocs.io/en/latest/02-models.html
"""

import django
from django.db import models
from django.contrib import auth
from django.test import TestCase

import accounts
from accounts.models import Profile
import dictionary
from dictionary.models import *

#Test Models
class ProfileTestCase(TestCase):
    """
    Test class to test Profile Model
    """
    def setUp(self):
        self.french = Language.objects.create(name="French")
        self.syrian_arabic = Language.objects.create(name="Syrian_Arabic")
        self.palestinian_arabic = Language.objects.create(name="Palestinian_Arabic")
        self.english = Language.objects.create(name="English")
        self.testuser1 = User.objects.create(
                username='testuser1',
                password='1z2x3c4v')
        self.testuser2 = User.objects.create(
                username='testuser2',
                password='1z2x3c4v')
        # self.testuser2.profile.native_languages.add(self.english)
        # self.testuser2.profile.target_dialects.add(self.palestinian_arabic)
        # self.testuser2.profile.target_dialects.add(self.syrian_arabic)
        # self.testuser2.save()

    def test_profile_created_when_user_created(self):
        self.assertIsNotNone(self.testuser1.profile)

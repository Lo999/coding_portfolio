"""
Barser Views
"""

from __future__ import unicode_literals
import string
import re
import logging
import nltk

import django
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import generic
import googletrans
from googletrans import Translator

import barser
from barser.models import *

class BarserView(generic.View):
"""
Barser view that accepts submission of
"""
    def get(self, request):

    def post(self, request):
        """
        Parse a webpage by gathering all visible text, pre processing it by
        removing non-arabic characters, using google translate to generate
        definitions, and creating entries out of the result.
        """
        text = TextForm(request)
        if text.is_valid():

            self.context["entries"] = zip(words, defs)

        self.context['url'] = url

class Barser:

    def

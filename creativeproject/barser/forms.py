"""
Barser Forms
"""

import requests
import string

import django
from django import forms
import bs4
from bs4 import BeautifulSoup
import alphabet_detector #https://github.com/EliFinkelshteyn/alphabet-detector
from alphabet_detector import AlphabetDetector

class TextForm(forms.Form):
    """
    Form used to generate arabic words from a URL
    """
    url = forms.URLField()
    text = forms.CharField(max_length=1000)

    def clean(self):
        """
        Overwrite of clean method to check that URL exists and get page text
        """
        try:
            r = requests.get(self.url)
            self.text = r.text
        except Error as e:
            print(e)
            raise forms.ValidationError("That URL does not exist")
        super(TextForm, self).clean()

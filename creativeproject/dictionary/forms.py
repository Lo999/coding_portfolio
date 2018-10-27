from django import forms
from dictionary.models import *

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['author',
                'script_word',
                'arabizi_word',
                'part_of_speech',
                'definition',
                'dialect']

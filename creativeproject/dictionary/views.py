"""
Dictionary Views
"""

import re
import json

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.views import generic

from dictionary.forms import *
from dictionary.models import *
from dictionary import validators

# Main Views

class SearchView(generic.ListView):
    """
    Search View, displays results of a search.
    Extends ListView and uses "entry" as its model.
    Url args stored in self: request, translation, dialect, word
    """
    model = Entry

    def get_queryset(self):
        """
        Searches database for entries based on client supplied get parameters
        """
        entries = Entry.objects.filter(dialect=self.kwargs['dialect'])
        if self.kwargs['translation']=='enar':
            entries = entries.filter(definition__icontains=self.kwargs['word'])
        elif validators.contains_arabic(word):
            entries = entries.filter(script_word=self.kwargs['word'])
        else:
            entries = entries.filter(arabizi_word=self.wargs['word'])
        return entries

    def get_context_data(self, **kwargs):
        """
        Gets additional context information for rendering
        """
        context = super(SearchView, self).get_context_data(**kwargs)
        entries = context['entry_list']
        comments = [c for e in entries for c in Comment.objects.filter(entry=e)]
        context['comments'] = comments
        return context

class EntryView(generic.View):
    """
    Create Entry View
    """
    def get(self, request):
        """
        Renders view for a get request
        """
        return render(request, 'dictionary/entry.html')

    def post(self, request):
        """
        Renders view for a post request
        """
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save()
        context = dict(form=form, entry=entry)
        return render(request, 'dictionary/entry.html',context)

def homepage(request):
    """
    Homepage View
    """
    return render(request, 'dictionary/homepage.html')

# Helper Functions

"""
Forum Views
"""

import re
import json

import django
from django.shortcuts import render, redirect
from django.core import serializers
from django.views import generic

import dictionary
import accounts
from dictionary import validators

# Create your views here.

class CommentView(generic.View):
    """
    Comment View
    """
    def get(request):
        search_url = request.POST.get('search_url')
        return render(
                request,
                'dictionary/comment.html',
                dict(search_url=search_url))

    def post(request):
        message=""
        if request.method == 'POST':
            entry = Entry.objects.get(pk=request.POST.get('pk'))
            comment = Comment(
                author=request.user.username,
                entry=entry,
                content=request.POST.get('content'),
                likes=0,
            )
            comment.save()
            message='success'
            return HttpResponseRedirect('/dictionary/homepage')
        else:
            message = "not posted"
            return HttpResponseRedirect('/dictionary/homepage')

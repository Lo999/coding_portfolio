"""
Forum Admin
"""

import django
from django.contrib import admin

import forum
from forum.models import Comment

class CommentAdmin(admin.ModelAdmin):
    fields = ['author', 'entry', 'content', 'likes']

admin.site.register(Comment, CommentAdmin)

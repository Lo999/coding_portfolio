"""
Forum URLS
"""

import re

import django
from django.conf.urls import url

import forum
from forum import views as forum_views

app_name = 'dictionary'

urlpatterns = [
    url(r'^comment/$', forum_views.CommentView.as_view(), name='comment'),
]

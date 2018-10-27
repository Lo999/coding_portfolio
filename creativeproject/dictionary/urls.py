"""
Dictionary URLS
"""

import re

import django
from django.conf.urls import url

import dictionary
from dictionary import views as dictionary_views

app_name = 'dictionary'

urlpatterns = [
    url(r'^$', dictionary_views.homepage, name='homepage'),
    url(
            r'^(?P<translation>(enar|aren))/(?P<dialect>[A-Za-z0-9_]*)/(?P<word>([\u0600-\u06FF]*|[A-Za-z0-9_]*))/$',
            dictionary_views.SearchView.as_view(),
            name='search'),
    url(r'^create/$', dictionary_views.EntryView.as_view(), name='entry'),
]

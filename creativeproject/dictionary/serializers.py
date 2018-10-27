"""
Dictionary Serializers
(currently not implemented)
"""

import django
from django.core import serializers

import dictionary
from dictionary import models as dictionary_models

def serialize_entries(entries):
    results = dict()
    i = 1
    for e in entries :
        e_id = ("entry%s" % i)
        results[e_id] = dict(
                author=e.author,
                script_word=e.script_word,
                arabizi_word=e.arabizi_word,
                part_of_speech=e.part_of_speech,
                definition=e.definition,
                dialect=e.dialect)
        i += 1
    return results

def serialize_comments(comments):
    results = dict()
    i = 1
    for c in comments :
        c_id = ("comment%s" % i)
        entry = serialize_entries([c.entry])
        results[c_id] = dict(
                author=c.author,
                entry=entry,
                content=c.content,
                likes=c.likes)
        i += 1
    return results

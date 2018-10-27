from django.contrib import admin
from dictionary.models import *

class EntryAdmin(admin.ModelAdmin):
    fields = [
            'author',
            'script_word',
            'arabizi_word',
            'part_of_speech',
            'definition',
            'dialect']

admin.site.register(Entry, EntryAdmin)
admin.site.register(Language)

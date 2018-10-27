"""
Dictionary Validators
documentation: https://docs.djangoproject.com/en/2.0/ref/validators/
used to verify entry fields
"""

import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Main Validators

def validate_arabic(word):
    if not contains_arabic(word):
        raise ValidationError(
            _('%(word)s does not contain Arabic script'),
            params=dict(word=word),
        )

def validate_not_arabic(word):
    if contains_arabic(word):
        raise ValidationError(
            _('%(word)s contains Arabic script'),
            params=dict(word=word),
        )

# Helper Methods

def contains_arabic(word):
    a = re.compile('[\u0600-\u06FF]')
    m = a.match(word)
    return m is not None

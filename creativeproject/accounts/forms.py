import django

import dictionary
import accounts

class UserForm(django.contrib.auth.forms.UserCreationForm):
    """
    Modified User Creation Form
    """
    class Meta:
        model = django.contrib.auth.models.User
        fields = ['username', 'password1']

class ProfileForm(django.forms.ModelForm):
    """
    User Profile form
    """
    class Meta:
        model = accounts.models.Profile
        fields = ['native_languages', 'target_dialects']

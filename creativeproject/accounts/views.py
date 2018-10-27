"""
Accounts Views
"""

import django
from django.shortcuts import redirect
from django.shortcuts import render

from accounts import forms
from accounts import models

# Main Functions

def register(request):
    """
    Registration View
    """
    if request.method != 'POST':
        uform = forms.UserForm()
        pform = forms.ProfileForm()
    else:
        uform = forms.UserForm(request.POST)
        pform = forms.ProfileForm(request.POST)
        if uform.is_valid() and pform.is_valid():
            create_user(uform, pform)
            auth_and_login(request, uform)
            return redirect('dictionary:homepage')
    context = dict(
            uform=uform,
            pform=pform)
    return render(request, 'registration/register.html', context)

# Helper Functions

def create_user(uform, pform):
    """
    Handles creation of a user and their profile from two forms
    """
    user = uform.save()
    profile = pform.save(commit=False)
    profile.user = user
    profile.save()

def auth_and_login(request, form):
    """
    Authenticates and logs in a user
    """
    username = form.cleaned_data.get('username')
    raw_password = form.cleaned_data.get('password1')
    user = django.contrib.auth.authenticate(
            username=username,
            password=raw_password)
    django.contrib.auth.login(request, user)

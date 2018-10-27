"""
Accounts Models
"""

import django
from django.db import models
from django.contrib import auth
from django.dispatch import receiver

import dictionary
from dictionary.models import Language

class Profile(models.Model):
    """
    Profile class that has a 1-to-1 relationship with Users.
    Used to store information about a speakers language knowledge and interests.
    """
    user = models.OneToOneField(
            auth.models.User,
            on_delete=models.CASCADE,
            primary_key=True,
            blank=False)
    native_languages = models.ManyToManyField(
            Language,
            blank=False,
            related_name="native_languages")
    target_dialects = models.ManyToManyField(
            Language,
            blank=False,
            related_name="target_languages")

    def __str__(self):
        return self.user.username


#SOURCE: https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
@receiver(
        models.signals.post_save,
        sender=auth.models.User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(
        models.signals.post_save,
        sender=auth.models.User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

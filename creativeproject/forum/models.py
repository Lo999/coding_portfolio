"""
Forum Models
"""

from django.db import models

import dictionary
from dictionary import models as dictionary_models

# Create your models here.
class Comment(models.Model):
    """
    Comment Model
    """
    author = models.CharField(max_length=30)
    entry = models.ForeignKey(dictionary_models.Entry, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    likes = models.PositiveSmallIntegerField()

    def __str__(self):
        return "author: %s, entry: %s, likes: %s" % (
                self.author,
                self.entry,
                self.likes)

    # def liked(self, user):
    #     codename = 'cant_like_' + str(self.pk)
    #     p = Permission.objects.get(codename=codename)
    #     user.user_permissions.add(p)
    #
    # def unliked(self, user):
    #     codename = 'cant_like_' + str(self.pk)
    #     p = Permission.objects.get(codename=codename)
    #     user.user_permissions.remove(p)

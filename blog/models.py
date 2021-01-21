from django.conf import settings
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, default='', blank=True)
    text = models.TextField()
    page = models.IntegerField()
    media = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        if self.title != '':
            return self.title
        else:
            return str('Post ' + str(self.id) + ', Page ' + str(self.page))

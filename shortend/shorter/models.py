from __future__ import unicode_literals
from django.db import models

from .utils import code_generator,create_shortcode


class shortUrlManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(shortUrlManager, self).all(*args,**kwargs)
        qs = qs_main.filter(active = True)
        return qs

    def refresh_shortcodes(self):
        qs = shortUrl.objects.filter(id__gte =1)
        newCodesGenrated = 0

        for q in qs:
            q.shortcode = create_shortcode(6)
            q.save()
            newCodesGenrated += 1

        return newCodesGenrated



class shortUrl(models.Model):
    url = models.CharField(max_length=220, )
    shortCode = models.CharField(max_length=15, unique = True)
    updated = models.DateTimeField(auto_now=True)
    timeStamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = shortUrlManager()

    def save(self, *args, **kwargs):
        self.shortCode = code_generator()
        super(shortUrl, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

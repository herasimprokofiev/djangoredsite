from django.db import models
from django.urls import reverse


class Newsfield(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def _str_(self):
        return self.title[:50]

    def get_absolute_url(self):
        return reverse('t', args=[str(self.id)])
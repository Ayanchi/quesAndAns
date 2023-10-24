from django.db import models

from sites.models import SiteFiles


class SomeLinks(models.Model):
    link = models.URLField(max_length=500)

    def __str__(self):
        return self.link


class Link(models.Model):
    links = models.ManyToManyField(SomeLinks, related_name="related_links")
    site_id = models.ForeignKey(SiteFiles, on_delete=models.CASCADE)

    def __str__(self):
        return self.links

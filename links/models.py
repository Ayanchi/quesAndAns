from django.db import models

from sites.models import SiteFiles


class SomeLinks(models.Model):
    link = models.URLField(max_length=500)
    site_id = models.ForeignKey(SiteFiles, on_delete=models.CASCADE)

    def __str__(self):
        return self.link


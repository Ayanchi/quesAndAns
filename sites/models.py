
from django.db import models


class SiteFiles(models.Model):
    file = models.FileField(upload_to='site_files')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return str(self.file)

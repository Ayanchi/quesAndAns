from django.db import models

from sites.models import SiteFiles


class QuestionAnswer(models.Model):
    question = models.TimeField(max_length=400)
    answer = models.TimeField(max_length=600)
    # site_id = models.ForeignKey(SiteFiles, on_delete=models.CASCADE)

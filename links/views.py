from django.shortcuts import render
from rest_framework import generics

from links.models import SomeLinks
from links.serializer import LinkSerializer


class LinkAPI(generics.ListAPIView):
    serializer_class = LinkSerializer

    def get_queryset(self):
        site_id = self.kwargs['site_id']
        return SomeLinks.objects.filter(site_id=site_id)
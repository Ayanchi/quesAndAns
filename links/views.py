from django.shortcuts import render
from rest_framework import generics

from links.models import Link
from links.serializer import LinkSerializer


class LinkAPI(generics.ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
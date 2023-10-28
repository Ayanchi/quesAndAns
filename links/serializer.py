from rest_framework import serializers

from links.models import SomeLinks


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomeLinks
        fields = ('site_id', 'link')

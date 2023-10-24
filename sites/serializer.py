from rest_framework import serializers

from sites.models import SiteFiles


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteFiles
        fields = ('file', 'time_create', 'id')
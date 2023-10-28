import re
from xml.etree import ElementTree

from rest_framework import generics, status
from rest_framework.response import Response

from links.models import SomeLinks
from sites.models import SiteFiles
from sites.serializer import SiteSerializer


class SiteAPI(generics.ListAPIView):
    queryset = SiteFiles.objects.all()
    serializer_class = SiteSerializer

    def post(self, request, *args, **kwargs):
        site_file = SiteFiles()
        site_file.file = request.data['file']
        site_file.save()

        print(site_file)

        with open(site_file.file.path, 'r') as f:
            content = f.read()

        cleaned_content = re.sub(r'^.*?<\?xml', '<?xml', content, flags=re.DOTALL)

        root = ElementTree.fromstring(cleaned_content)

        # Search for all the <loc> tags and extract their text content.
        namespaces = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

        # Search for all the <loc> tags within the namespace and extract their text content.
        urls = [elem.text for elem in root.findall('.//sm:loc', namespaces)]

        for url in urls:
            SomeLinks.objects.create(link=url, site_id=site_file)

        return Response({'message': 'Файл успешно сохранен'}, status=status.HTTP_201_CREATED)

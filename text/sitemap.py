# from django.contrib.sitemaps import Sitemap
# from django.core.files.base import ContentFile
# from django.conf import settings
#
# from sites.models import Site
#
# import os
# import requests
#
# file_directory = os.path.join(settings.MEDIA_ROOT, 'site_files')
# os.makedirs(file_directory, exist_ok=True)
#
#
# class SiteSitemap(Sitemap):
#     changefreq = "weekly"
#     priority = 0.5
#
#     def items(self):
#         current_site_domain = Site.objects.all()
#         for site in current_site_domain:
#             return Site.objects.filter(is_published=True)
#
#     def lastmod(self, obj):
#         return obj.time_create
#
#
# # Вывод результата
# print(SiteSitemap().items())

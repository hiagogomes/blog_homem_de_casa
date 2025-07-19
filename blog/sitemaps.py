# blog/sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['home', 'sobre', 'contato', 'politica_privacidade', 'politica_afiliado', 'termos_uso']

    def location(self, item):
        return reverse(item)

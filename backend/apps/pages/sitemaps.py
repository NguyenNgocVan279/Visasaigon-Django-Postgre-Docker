from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = "https"

    def items(self):
        return [
            "pages:trang-chu",
            "pages:gioi-thieu",
            "pages:lien-he",

            "visa:visa-cac-nuoc",
            "visa:ho-so-yeu-cau",
        ]

    def location(self, item):
        return reverse(item)
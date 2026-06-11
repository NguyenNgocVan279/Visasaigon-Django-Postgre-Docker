from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Country


class CountrySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    protocol = "https"

    def items(self):
        return Country.objects.all()

    def location(self, obj):
        return reverse(
            "visa:country_detail",
            kwargs={"country_slug": obj.slug}
        )

    def lastmod(self, obj):
        return obj.updated_at
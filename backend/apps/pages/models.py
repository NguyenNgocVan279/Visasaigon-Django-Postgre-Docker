from django.db import models
from apps.core_app.models import TimeStampedModel

class Page(TimeStampedModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    featured_image = models.ImageField(
        upload_to="pages/",
        blank=True,
        null=True,
        help_text="Ảnh đại diện của trang"
    )
    content = models.TextField()

    def __str__(self):
        return self.title

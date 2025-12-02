from django.db import models
from apps.core_app.models import TimeStampedModel
from ckeditor.fields import RichTextField

class Page(TimeStampedModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    featured_image = models.ImageField(
        upload_to="pages/",
        blank=True,
        null=True,
        help_text="Ảnh đại diện của trang"
    )
    content = RichTextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Trang tĩnh"
        verbose_name_plural = "Trang tĩnh"

from django.db import models
from apps.core_app.models import TimeStampedModel
from ckeditor.fields import RichTextField


class CompanyProfile(TimeStampedModel):
    name = models.CharField(max_length=255)
    domain = models.URLField(blank=True)
    logo = models.ImageField(upload_to="company/") # Lưu vào media\company\logo.png
    hotline = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    google_map = models.TextField(blank=True)

    facebook = models.URLField(blank=True)
    tiktok = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    zalo = models.URLField(blank=True)

    description = RichTextField(blank=True)
    normal_working_time = models.CharField(
        blank=True,
        help_text="Nhập giờ làm việc, ví dụ: '08:00-17:00'"
    )
    saturday_working_time = models.CharField(
        blank=True,
        help_text="Nhập giờ làm việc, ví dụ: '08:00-17:00'"
    )
    web_dev_partner = models.CharField(max_length=255)
    partner_web_link = models.URLField(blank=True)


    class Meta:
        verbose_name = "Company Profile"
        verbose_name_plural = "Company Profile"

    def __str__(self):
        return self.name

from django.db import models
from apps.core_app.models import TimeStampedModel
from ckeditor.fields import RichTextField

class Country(TimeStampedModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, blank=True, null=True)  # ISO code
    region = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True)

    # New fields
    cover_image = models.ImageField(upload_to="visa/country/covers/", blank=True, null=True)
    flag_image = models.ImageField(upload_to="visa/country/flags/", blank=True, null=True)

    class Meta:
        verbose_name = "Quốc gia"
        verbose_name_plural = "Quốc gia"

    def __str__(self):
        return self.name

class VisaType(TimeStampedModel):
    PURPOSE_CHOICES = [
        ('family_visit', 'Thăm người thân'),
        ('tourism', 'Du lịch'),
        ('business', 'Công tác'),
        ('student', 'Du học'),
        ('work', 'Lao động'),
        ('other', 'Khác'),
    ]

    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="visa_types")
    name = models.CharField(max_length=255)
    description = RichTextField(blank=True)
    purpose = models.CharField(max_length=50, choices=PURPOSE_CHOICES, default='other')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.name} ({self.country.name} - {self.get_purpose_display()})"
    
    class Meta:
        verbose_name = "Loại visa"
        verbose_name_plural = "Loại visa"


class RequiredDocument(TimeStampedModel):
    """
    Giấy tờ yêu cầu phụ thuộc Country, VisaType
    """
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="required_documents")
    visa_type = models.ForeignKey(VisaType, on_delete=models.CASCADE, related_name='required_documents')
    name = models.CharField(max_length=255)
    description = RichTextField(blank=True)

    class Meta:
        unique_together = ('country', 'visa_type', 'name')
        verbose_name = "Yêu cầu hồ sơ"
        verbose_name_plural = "Yêu cầu hồ sơ"

    def __str__(self):
        return f"{self.name} ({self.visa_type.name} - {self.country.name})"


# ==========================
#  PHẦN CHO TRANG GIỚI THIỆU VISA THEO COUNTRY
#  Mô tả: class cho các table
# ==========================
class CountryDetail(TimeStampedModel):
    country = models.OneToOneField(
        Country, 
        on_delete=models.CASCADE, 
        related_name="detail"
    )
    hero_title = models.CharField(max_length=255, blank=True, null=True)
    hero_subtitle = models.CharField(blank=True, null=True)

    overview_title = models.CharField(max_length=255, blank=True, null=True)
    overview_content = RichTextField(blank=True, null=True)

    visa_types_summary = models.CharField(max_length=255, blank=True, null=True, help_text="Ví dụ: Visa du lịch, thăm thân, công tác")
    visa_processing_time = models.CharField(max_length=255, blank=True, null=True, help_text="Ví dụ: 10–30 ngày")
    visa_highlight_note_1 = models.CharField(max_length=255, blank=True, null=True)
    visa_highlight_note_2 = models.CharField(max_length=255, blank=True, null=True)
    visa_highlight_note_3 = models.CharField(max_length=255, blank=True, null=True)

    cta_title = models.CharField(max_length=255, blank=True, null=True)
    cta_featured_requirement_1 = models.CharField(blank=True, null=True)
    cta_featured_requirement_2 = models.CharField(blank=True, null=True)
    cta_featured_requirement_3 = models.CharField(blank=True, null=True)
    cta_featured_requirement_4 = models.CharField(blank=True, null=True)
    cta_subtitle = models.CharField(blank=True, null=True)
    cta_button_text = models.CharField(max_length=100, blank=True, null=True)
    cta_button_link = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Detail for {self.country.name}"
    
    class Meta:
        verbose_name = "Giới thiệu từng nước"
        verbose_name_plural = "Giới thiệu từng nước"


class CountrySection(TimeStampedModel):
    country = models.ForeignKey(
        Country, 
        on_delete=models.CASCADE, 
        related_name="sections"
    )
    title = models.CharField(max_length=255)
    content = RichTextField()
    image = models.ImageField(upload_to="visa/country/sections/", blank=True, null=True)
    image_left = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Các phần trang giới thiệu"
        verbose_name_plural = "Các phần trang giới thiệu"

    def __str__(self):
        return f"{self.title} ({self.country.name})"


class CountryTip(TimeStampedModel):
    TIP_CHOICES = [
        ("risk", "Rủi ro bị từ chối"),
        ("tip", "Mẹo tăng tỉ lệ đậu"),
    ]

    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="tips"
    )
    tip_type = models.CharField(max_length=20, choices=TIP_CHOICES)
    content = RichTextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Tip"
        verbose_name_plural = "Tips"

    def __str__(self):
        return f"{self.get_tip_type_display()} - {self.country.name}"

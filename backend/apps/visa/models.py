from django.db import models
from apps.core_app.models import TimeStampedModel

class Country(TimeStampedModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, blank=True, null=True)  # ISO code
    region = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Countries"

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
    description = models.TextField(blank=True)
    purpose = models.CharField(max_length=50, choices=PURPOSE_CHOICES, default='other')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.name} ({self.country.name} - {self.get_purpose_display()})"


class RequiredDocument(TimeStampedModel):
    """
    Giấy tờ yêu cầu phụ thuộc cả Country và VisaType
    """
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="required_documents")
    visa_type = models.ForeignKey(VisaType, on_delete=models.CASCADE, related_name='required_documents')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ('country', 'visa_type', 'name')
        verbose_name = "Required Document"
        verbose_name_plural = "Required Documents"

    def __str__(self):
        return f"{self.name} ({self.visa_type.name} - {self.country.name})"
    
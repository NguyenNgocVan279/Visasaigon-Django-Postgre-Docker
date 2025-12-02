from django.db import models
from apps.core_app.models import TimeStampedModel
from ckeditor.fields import RichTextField

class FAQCategory(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Danh mục FAQ"
        verbose_name_plural = "Danh mục FAQ"


class FAQItem(TimeStampedModel):
    question = models.CharField(max_length=255)
    answer = RichTextField()
    category = models.ForeignKey(FAQCategory,on_delete=models.SET_NULL,null=True,related_name="faqs")

    # 🔥 Thêm ManyToManyField để hiện thị cho trang coutry_detail.html
    countries = models.ManyToManyField(
        "visa.Country",
        blank=True,
        related_name="faqs"
    )

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Danh sách FAQ"
        verbose_name_plural = "Danh sách FAQ"
        

    def __str__(self):
        return self.question

from django.db import models
from apps.core_app.models import TimeStampedModel
from apps.visa.models import VisaType
from .utils import application_file_upload_path
from ckeditor.fields import RichTextField


# ============================================================
# CLIENT
# ============================================================
class Client(TimeStampedModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "Danh sách khách hàng"
        verbose_name_plural = "Danh sách khách hàng"


# ============================================================
# APPLICATION
# ============================================================
class Application(TimeStampedModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="applications")
    visa_type = models.ForeignKey(VisaType, on_delete=models.SET_NULL, blank=True, null=True)

    # -------- Travel info --------
    SOLO_OR_GROUP_CHOICES = [
        ('solo', 'Đi một mình'),
        ('group', 'Đi theo nhóm / gia đình'),
    ]
    solo_or_group_travel = models.CharField(
        max_length=20,
        choices=SOLO_OR_GROUP_CHOICES,
        default='solo',
        verbose_name="Đi một mình hay theo nhóm"
    )
    
    travel_history_countries = models.CharField(max_length=255, blank=True, null=True)
    
    # -------- Family members --------
    family_members = RichTextField(
        blank=True,
        null=True
    )

    # -------- Occupation --------
    OCCUPATION_CHOICES = [
        ('business_owner', 'Chủ DN / Tự doanh'),
        ('employee', 'Nhân viên công ty'),
        ('freelance', 'Lao động tự do'),
        ('retired', 'Đã nghỉ hưu'),
        ('homemaker', 'Nội trợ'),
        ('student', 'Sinh viên'),
        ('pupil', 'Học sinh'),
        ('other', 'Khác'),
    ]
    occupation = models.CharField(max_length=50, choices=OCCUPATION_CHOICES, blank=True, null=True)

    # -------- Inviter info --------
    inviter_full_name = models.CharField(max_length=255, blank=True, null=True)
    inviter_dob = models.DateField(blank=True, null=True)
    inviter_address = models.CharField(max_length=500, blank=True, null=True)
    inviter_phone = models.CharField(max_length=50, blank=True, null=True)
    inviter_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"Application #{self.id} - {self.client}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Đăng ký dịch vụ"
        verbose_name_plural = "Đăng ký dịch vụ"


# ============================================================
# APPLICATION FILE
# ============================================================
class ApplicationFile(TimeStampedModel):
    FILE_TYPE_CHOICES = [
        ('passport', 'Hộ chiếu'),
        ('id_card', 'CCCD'),
        ('invitation', 'Thư mời'),
        ('financial', 'Giấy tờ tài chính'),
        ('personal', 'Giấy tờ cá nhân'),
        ('other', 'Giấy tờ khác'),
    ]

    application = models.ForeignKey(
        "clients.Application",
        on_delete=models.CASCADE,
        related_name="files"
    )

    client_name = models.CharField(max_length=255, blank=True, null=True)

    file_type = models.CharField(max_length=50, choices=FILE_TYPE_CHOICES)

    # Hàm upload custom
    file = models.FileField(upload_to=application_file_upload_path)

    def save(self, *args, **kwargs):
        if self.application:
            self.client_name = f"{self.application.client.last_name} {self.application.client.first_name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.file_type} - {self.client_name}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "File khách hàng gửi"
        verbose_name_plural = "File khách hàng gửi"


from django.db import models
from apps.core_app.models import TimeStampedModel
from apps.visa.models import VisaType


# ============================================================
# CLIENT
# ============================================================
class Client(TimeStampedModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "Client"
        verbose_name_plural = "Clients"


# ============================================================
# APPLICATION
# ============================================================
class Application(TimeStampedModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="applications")
    visa_type = models.ForeignKey(VisaType, on_delete=models.SET_NULL, null=True)

    # -------- Travel info --------
    travel_alone = models.BooleanField(default=True)
    travel_history_countries = models.TextField(
        blank=True,
        null=True,
        help_text="Ví dụ: Singapore, Malaysia, Thailand"
    )

    # -------- Family members (JSONField) --------
    family_members = models.JSONField(
        blank=True,
        default=list,
        help_text="Danh sách thân nhân: [{'full_name':'','dob':'','current_address':'','relation':''}, ...]"
    )

    # -------- Occupation --------
    OCCUPATION_CHOICES = [
        ('business_owner', 'Chủ DN / Tự doanh'),
        ('employee', 'Nhân viên công ty'),
        ('retired', 'Đã nghỉ hưu'),
        ('homemaker', 'Nội trợ'),
        ('student', 'Sinh viên'),
        ('pupil', 'Học sinh'),
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
        verbose_name = "Application"
        verbose_name_plural = "Applications"


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

    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name="files")
    file_type = models.CharField(max_length=50, choices=FILE_TYPE_CHOICES)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    client_name = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.application:
            self.client_name = f"{self.application.client.last_name} {self.application.client.first_name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.file_type} - {self.client_name}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Application File"
        verbose_name_plural = "Application Files"

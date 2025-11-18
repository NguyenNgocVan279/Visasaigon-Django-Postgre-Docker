from django.contrib import admin
from django import forms
from .models import Client, Application, ApplicationFile


# ============================================================
# FORM: ApplicationFileForm (tự động fill client_name bằng JS)
# ============================================================
class ApplicationFileForm(forms.ModelForm):
    class Meta:
        model = ApplicationFile
        fields = "__all__"

    class Media:
        js = ("admin/js/applicationfile_autofill.js",)


# ============================================================
# ADMIN: Client
# ============================================================
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "email", "phone")
    search_fields = ("first_name", "last_name", "email", "phone")
    list_filter = ("created_at",)


# ============================================================
# ADMIN: Application
# ============================================================
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "client", "visa_type", "travel_alone", "created_at")
    search_fields = ("client__first_name", "client__last_name")
    list_filter = ("visa_type", "travel_alone", "created_at")
    autocomplete_fields = ("client", "visa_type")


# ============================================================
# ADMIN: ApplicationFile
# ============================================================
@admin.register(ApplicationFile)
class ApplicationFileAdmin(admin.ModelAdmin):
    form = ApplicationFileForm

    list_display = ("file_type", "client_name", "application", "created_at")
    search_fields = ("client_name", "application__client__first_name", "application__client__last_name")
    autocomplete_fields = ("application",)

    class Media:
        js = ("admin/js/applicationfile_autofill.js",)

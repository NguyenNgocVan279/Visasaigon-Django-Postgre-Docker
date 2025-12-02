from django import forms
from django.forms import modelformset_factory
from .models import Client, Application, ApplicationFile
from django.utils.safestring import mark_safe
from ckeditor.widgets import CKEditorWidget


# -------------------------------------------------
# Base Styled Form
# -------------------------------------------------
class BaseStyledForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            widget = field.widget

            if isinstance(widget, (forms.RadioSelect, forms.CheckboxInput, forms.CheckboxSelectMultiple, forms.ClearableFileInput)):
                continue

            existing_class = widget.attrs.get("class", "")
            widget.attrs["class"] = f"{existing_class} form-control".strip()

# -------------------------------------------------
# Client Form
# -------------------------------------------------
class ClientForm(BaseStyledForm):
    class Meta:
        model = Client
        fields = [
            "first_name", "last_name", "phone", "email", "date_of_birth"
        ]
        labels = {
            "first_name": "Họ", 
            "last_name": "Tên đệm & Tên", 
            "phone": "Số điện thoại", 
            "email": "Địa chỉ email", 
            "date_of_birth": "Ngày sinh"
        }
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
        }

# -------------------------------------------------
# Application Form
# -------------------------------------------------
class ApplicationForm(BaseStyledForm):
    class Meta:
        model = Application
        fields = [
            "visa_type",
            "solo_or_group_travel",
            "travel_history_countries",
            "occupation",
            "family_members",
            "inviter_full_name",
            "inviter_dob",
            "inviter_address",
            "inviter_phone",
            "inviter_email",
        ]
        labels = {
            "visa_type": "Loại visa",
            "solo_or_group_travel": "Đi một mình hay nhiều người",
            "travel_history_countries": "Đã từng đi nước nào",
            "occupation": "Nghề nghiệp",
            "family_members": "Thông tin người thân (cha, mẹ, anh chị em ruột)",
            "inviter_full_name": "Họ tên người mời",
            "inviter_dob": "Ngày sinh người mời",
            "inviter_address": "Địa chỉ người mời",
            "inviter_phone": "Số điện thoại người mời",
            "inviter_email": "Email người mời"
        }
        widgets = {
            "inviter_dob": forms.DateInput(attrs={"type": "date"}),
            "family_members": CKEditorWidget(
                attrs={
                    "rows": 8,
                    "placeholder": mark_safe(
                        "Bố: Nguyễn Văn A, SN: 01/01/1945, Nơi ở: 123, Đường Trần Não, P. An Khánh, TP.HCM\n"
                        "Mẹ: Nguyễn Thị B, SN: 01/01/1948, Nơi ở: 123, Đường Trần Não, P. An Khánh, TP.HCM"
                    ),
                    "class": "form-control placeholder-style",
                }
            ),
            "solo_or_group_travel": forms.RadioSelect(
                attrs={
                    "class": "form-check-input ms-3 me-2"
                }
            ),
            "visa_type": forms.Select(attrs={"class": "form-select"}),
            "occupation": forms.Select(attrs={"class": "form-select"})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["family_members"].help_text = mark_safe(self.fields["family_members"].help_text)
        # Thêm placeholder ở đầu choices
        self.fields['visa_type'].choices = [('', '-----Vui lòng chọn-----')] + [
            choice for choice in self.fields['visa_type'].choices if choice[0]
        ]
        self.fields['occupation'].choices = [('', '-----Vui lòng chọn-----')] + [
            choice for choice in self.fields['occupation'].choices if choice[0]
        ]


# -------------------------------------------------
# Application File Form (mỗi dòng 1 file)
# -------------------------------------------------
class ApplicationFileForm(BaseStyledForm):
    class Meta:
        model = ApplicationFile
        fields = ["file_type", "file"]
        labels = {
            "file_type": "Loại file", 
            "file": "Upload file"
        }
        widgets = {
            "file": forms.ClearableFileInput(),  # ⛔ KHÔNG dùng multiple
            "file_type": forms.Select(attrs={"class": "form-select"})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file_type'].choices = [('', '-----Vui lòng chọn-----')] + [
            choice for choice in self.fields['file_type'].choices if choice[0]
        ]


# -------------------------------------------------
# FORMSET
# -------------------------------------------------
ApplicationFileFormSet = modelformset_factory(
    ApplicationFile,
    form=ApplicationFileForm,
    extra=1,            # số dòng mặc định
    can_delete=True     # cho phép xóa dòng
)

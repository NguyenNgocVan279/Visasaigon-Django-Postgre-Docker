from django.core.management.base import BaseCommand
from django.utils.text import slugify
from apps.visa.models import Country, VisaType, RequiredDocument


class Command(BaseCommand):
    help = "Seed dữ liệu: Yêu cầu hồ sơ Visa Công tác Canada"

    def handle(self, *args, **options):
        # 1. Country
        country_name = "Canada"
        country, _ = Country.objects.get_or_create(
            name=country_name,
            defaults={
                "code": "CA",
                "region": "Bắc Mỹ",
                "slug": slugify(country_name),
            },
        )

        # 2. VisaType
        visa_type_name = "Visa Công tác Canada"
        visa_type, _ = VisaType.objects.get_or_create(
            country=country,
            name=visa_type_name,
            defaults={
                "description": "Visa dùng để tham gia hội nghị, họp đối tác, ký kết hợp đồng hoặc các hoạt động công tác khác tại Canada.",
                "purpose": "business",
                "slug": slugify(visa_type_name),
            },
        )

        # 3. DESCRIPTION FORMAT
        description_text = """
1. HỒ SƠ NHÂN THÂN
- Hộ chiếu còn hạn tối thiểu 6 tháng.
- CCCD/CMND.
- Sổ hộ khẩu (bản sao đầy đủ).
- Ảnh 4x6 nền trắng (tùy thời điểm yêu cầu).
- Giấy đăng ký kết hôn (nếu đã kết hôn).

2. HỒ SƠ CÔNG VIỆC
**Đối với nhân viên**
- Hợp đồng lao động.
- Quyết định cử đi công tác (bản gốc hoặc bản sao công ty ký).
- Xác nhận công việc từ công ty.
- Bảng lương 3–6 tháng gần nhất.
- Giấy tờ chứng minh chức vụ hoặc nhiệm vụ công tác.

**Đối với chủ doanh nghiệp**
- Giấy phép kinh doanh.
- Biên bản cử người đi công tác (nếu không trực tiếp đi).
- Tài liệu thể hiện hoạt động kinh doanh thực tế.

3. CHỨNG MINH TÀI CHÍNH
- Sao kê ngân hàng 3–6 tháng.
- Tài sản sở hữu: nhà đất, xe ô tô, tài sản có giá trị.
- Chứng minh thu nhập ổn định.
- Nếu công ty tài trợ chi phí:
+ Thư bảo lãnh chi trả chi phí công tác.
+ Sao kê tài khoản hoặc báo cáo tài chính của công ty.

4. GIẤY TỜ CÔNG TÁC TỪ CANADA
- Thư mời công tác (Invitation Letter) từ doanh nghiệp/đối tác Canada.
- Lịch trình làm việc (Meeting schedule / Agenda).
- Tài liệu chứng minh quan hệ hợp tác:
+ Email trao đổi.
+ Hợp đồng nguyên tắc, hợp đồng thương mại, MOU.
- Giấy tờ đăng ký kinh doanh của công ty Canada (nếu có).

5. GIẤY TỜ CHUYẾN ĐI
- Booking khách sạn hoặc giấy xác nhận nơi ở.
- Vé máy bay dự kiến (có thể không bắt buộc).
- Bảo hiểm du lịch (nếu được yêu cầu).

6. THƯ GIẢI TRÌNH
- Nêu rõ mục đích chuyến đi.
- Thời gian dự kiến làm việc.
- Cam kết quay về Việt Nam sau chuyến công tác.

7. LƯU Ý QUAN TRỌNG
- Thư mời công tác phải nêu rõ mục đích, thời gian và người phụ trách tại Canada.
- Hồ sơ công ty và hồ sơ cá nhân cần minh bạch, đồng nhất.
- Không nên kê khai mục đích không đúng thực tế.
- Lãnh sự có thể yêu cầu bổ sung giấy tờ hoặc phỏng vấn.
"""

        # 4. Create RequiredDocument
        RequiredDocument.objects.get_or_create(
            country=country,
            visa_type=visa_type,
            name="Yêu cầu hồ sơ Visa Công tác Canada",
            defaults={"description": description_text},
        )

        self.stdout.write(self.style.SUCCESS("✔ Seed Visa Công tác Canada (format chuẩn) thành công!"))

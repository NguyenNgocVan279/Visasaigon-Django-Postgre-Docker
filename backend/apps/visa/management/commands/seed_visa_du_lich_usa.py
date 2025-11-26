from django.core.management.base import BaseCommand
from django.utils.text import slugify
from apps.visa.models import Country, VisaType, RequiredDocument


class Command(BaseCommand):
    help = "Seed dữ liệu: Yêu cầu hồ sơ Visa Du lịch Hoa Kỳ"

    def handle(self, *args, **options):
        # 1. Country
        country_name = "Hoa Kỳ"
        country, _ = Country.objects.get_or_create(
            name=country_name,
            defaults={
                "code": "US",
                "region": "Bắc Mỹ",
                "slug": slugify(country_name),
            },
        )

        # 2. VisaType
        visa_type_name = "Visa Du lịch Hoa Kỳ"
        visa_type, _ = VisaType.objects.get_or_create(
            country=country,
            name=visa_type_name,
            defaults={
                "description": "Visa B1/B2 dùng cho mục đích du lịch, thăm quan, nghỉ dưỡng hoặc thăm gia đình/người thân ngắn hạn tại Hoa Kỳ.",
                "purpose": "tourist",
                "slug": slugify(visa_type_name),
            },
        )

        # 3. DESCRIPTION FORMAT
        description_text = """
1. HỒ SƠ NHÂN THÂN
- Hộ chiếu còn hạn tối thiểu 6 tháng.
- CCCD/CMND.
- Giấy khai sinh.
- Sổ hộ khẩu (bản sao đầy đủ).
- Ảnh 5x5cm nền trắng đúng chuẩn Mỹ.
- Giấy đăng ký kết hôn (nếu đã kết hôn) hoặc giấy độc thân (nếu yêu cầu).
- Form DS-160 khai trực tuyến (bắt buộc).

2. HỒ SƠ CÔNG VIỆC
**Đối với nhân viên**
- Hợp đồng lao động.
- Xác nhận công việc.
- Đơn xin nghỉ phép du lịch.
- Bảng lương 3–6 tháng gần nhất.

**Đối với chủ doanh nghiệp**
- Giấy phép kinh doanh.
- Sao kê tài khoản doanh nghiệp 3–6 tháng.
- Tài liệu chứng minh hoạt động kinh doanh.

**Đối với người làm tự do**
- Tài liệu chứng minh nguồn thu nhập.
- Sao kê tài khoản ngân hàng.

**Đối với học sinh – sinh viên**
- Giấy xác nhận đang học.
- Thẻ học sinh/sinh viên.

3. CHỨNG MINH TÀI CHÍNH
- Sổ tiết kiệm hoặc sao kê ngân hàng 3–6 tháng.
- Chứng minh thu nhập ổn định.
- Tài sản sở hữu: sổ đỏ, ô tô, tài sản giá trị.
- Hồ sơ tài chính của người tài trợ (nếu có).

4. GIẤY TỜ LỊCH TRÌNH DU LỊCH
- Lịch trình tham quan tại Hoa Kỳ.
- Booking khách sạn (không bắt buộc nhưng khuyến khích).
- Vé máy bay dự kiến (tùy chọn).
- Bảo hiểm du lịch (không bắt buộc).

5. GIẤY TỜ BỔ SUNG (NẾU THĂM THÂN)
- Thư mời (Invitation Letter).
- Chứng minh quan hệ gia đình/họ hàng.
- Giấy tờ cư trú của người mời:
+ Thẻ xanh (Green Card), Visa Work/Study, hoặc Citizenship.
- Tài chính của người mời (nếu tài trợ chi phí).

6. HỒ SƠ CHO TRẺ EM (NẾU ĐI CÙNG)
- Giấy khai sinh.
- Hộ chiếu riêng.
- Giấy xác nhận học sinh.
- Giấy ủy quyền của cha/mẹ nếu chỉ một người đi.

7. LƯU Ý QUAN TRỌNG
- Visa du lịch Mỹ không yêu cầu nộp hồ sơ giấy trước, nhưng cần **chuẩn bị đủ để mang theo khi phỏng vấn**.
- Kết quả visa phụ thuộc mạnh vào **phỏng vấn tại Lãnh sự quán**.
- Cần chứng minh **ràng buộc quay về Việt Nam**: công việc, tài chính, gia đình.
- Không nên trình bày thông tin giả hoặc không nhất quán.
- Lãnh sự có quyền yêu cầu bổ sung tài liệu bất cứ lúc nào.
"""

        # 4. Create RequiredDocument
        RequiredDocument.objects.get_or_create(
            country=country,
            visa_type=visa_type,
            name="Yêu cầu hồ sơ Visa Du lịch Hoa Kỳ",
            defaults={"description": description_text},
        )

        self.stdout.write(self.style.SUCCESS("✔ Seed Visa Du lịch Hoa Kỳ (format chuẩn) thành công!"))

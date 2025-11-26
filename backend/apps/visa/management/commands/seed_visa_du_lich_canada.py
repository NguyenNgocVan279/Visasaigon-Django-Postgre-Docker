from django.core.management.base import BaseCommand
from django.utils.text import slugify
from apps.visa.models import Country, VisaType, RequiredDocument

class Command(BaseCommand):
    help = "Seed dữ liệu: Yêu cầu hồ sơ Visa Du lịch Canada"

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
        visa_type_name = "Visa Du lịch Canada"
        visa_type, _ = VisaType.objects.get_or_create(
            country=country,
            name=visa_type_name,
            defaults={
                "description": "Visa dành cho mục đích du lịch, tham quan và nghỉ dưỡng tại Canada.",
                "purpose": "tourism",
                "slug": slugify(visa_type_name),
            },
        )

        # 3. DESCRIPTION FORMAT (giống chuẩn bạn yêu cầu)
        description_text = """
1. HỒ SƠ NHÂN THÂN
- Hộ chiếu còn hạn tối thiểu 6 tháng.
- CCCD/CMND.
- Sổ hộ khẩu (bản sao đầy đủ).
- Giấy đăng ký kết hôn (nếu đã kết hôn).
- Ảnh 4x6 nền trắng (chụp trong 6 tháng).

2. HỒ SƠ CÔNG VIỆC
**Đối với nhân viên**
- Hợp đồng lao động.
- Bảng lương 3–6 tháng.
- Xác nhận công việc và đơn xin nghỉ phép.
- Quyết định cho phép nghỉ đi du lịch.

**Đối với chủ doanh nghiệp**
- Giấy phép kinh doanh.
- Sao kê ngân hàng doanh nghiệp 3–6 tháng.
- Tài liệu thuế (nếu có).

**Đối với lao động tự do**
- Chứng minh nguồn thu nhập hợp pháp.
- Sao kê tài khoản cá nhân 3–6 tháng.

**Đối với học sinh – sinh viên**
- Giấy xác nhận đang học.
- Thẻ học sinh/sinh viên.

3. CHỨNG MINH TÀI CHÍNH
- Sao kê ngân hàng 3–6 tháng.
- Sổ tiết kiệm (nếu có).
- Chứng minh tài sản: nhà, đất, xe cộ…
- Chứng minh ràng buộc tại Việt Nam: gia đình, công việc, tài sản.
- Nếu có người tài trợ → nộp hồ sơ tài chính của người tài trợ.

4. LỊCH TRÌNH CHUYẾN ĐI
- Lịch trình du lịch dự kiến tại Canada.
- Booking khách sạn hoặc xác nhận lưu trú.
- Vé máy bay dự kiến (không bắt buộc xuất vé).

5. THƯ GIẢI TRÌNH MỤC ĐÍCH CHUYẾN ĐI
- Nêu rõ lý do du lịch.
- Thời gian lưu trú dự kiến.
- Cam kết quay về Việt Nam sau chuyến đi.

6. HỒ SƠ DÀNH CHO TRẺ EM (NẾU CÓ)
- Giấy khai sinh.
- Hộ chiếu riêng của trẻ.
- Giấy xác nhận đang học tại trường.
- Nếu trẻ không đi cùng cha/mẹ:
+ Giấy đồng ý cho trẻ xuất cảnh có xác nhận.
- Hồ sơ tài chính và công việc dựa theo cha/mẹ.

7. LƯU Ý QUAN TRỌNG
- Canada xem xét kỹ **mục đích du lịch + ràng buộc quay về Việt Nam**.
- Hồ sơ tài chính phải thể hiện **nguồn tiền rõ ràng – ổn định**.
- Không nên ghi thời gian lưu trú quá dài so với công việc/tài chính tại Việt Nam.
- Lãnh sự Canada có thể yêu cầu bổ sung hoặc gọi xác minh.
- Hồ sơ càng rõ ràng – logic – minh bạch thì tỷ lệ đậu càng cao.
"""

        # 4. Create RequiredDocument
        RequiredDocument.objects.get_or_create(
            country=country,
            visa_type=visa_type,
            name="Yêu cầu hồ sơ Visa Du lịch Canada",
            defaults={"description": description_text},
        )

        self.stdout.write(self.style.SUCCESS("✔ Seed Visa Du lịch Canada (format chuẩn) thành công!"))

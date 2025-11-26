from django.core.management.base import BaseCommand
from django.utils.text import slugify
from apps.visa.models import Country, VisaType, RequiredDocument

class Command(BaseCommand):
    help = "Seed dữ liệu: Yêu cầu hồ sơ Visa Thăm thân Canada"

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
        visa_type_name = "Visa Thăm thân Canada"
        visa_type, _ = VisaType.objects.get_or_create(
            country=country,
            name=visa_type_name,
            defaults={
                "description": "Visa dùng để thăm người thân đang cư trú, học tập hoặc làm việc tại Canada.",
                "purpose": "family_visit",
                "slug": slugify(visa_type_name),
            },
        )

        # 3. DESCRIPTION FORMAT
        description_text = """
1. HỒ SƠ NHÂN THÂN
- Hộ chiếu còn hạn tối thiểu 6 tháng.
- CCCD/CMND.
- Sổ hộ khẩu (bản sao đầy đủ).
- Giấy khai sinh (để chứng minh quan hệ gia đình).
- Giấy đăng ký kết hôn (nếu đã kết hôn).
- Ảnh 4x6 nền trắng (tùy thời điểm yêu cầu).

2. HỒ SƠ CÔNG VIỆC
**Đối với nhân viên**
- Hợp đồng lao động.
- Bảng lương 3–6 tháng.
- Đơn xin nghỉ phép thăm thân.
- Xác nhận công việc từ công ty.

**Đối với chủ doanh nghiệp**
- Giấy phép kinh doanh.
- Sao kê tài khoản doanh nghiệp 3–6 tháng.
- Hồ sơ thuế (nếu có).

**Đối với lao động tự do**
- Giấy tờ chứng minh công việc và thu nhập thực tế.

**Đối với học sinh – sinh viên**
- Giấy xác nhận đang học.
- Thẻ học sinh/sinh viên.

3. CHỨNG MINH TÀI CHÍNH
- Sổ tiết kiệm hoặc sao kê ngân hàng 3–6 tháng.
- Chứng minh thu nhập đều đặn.
- Chứng minh tài sản: sổ đỏ, ô tô, tài sản khác.
- Nếu người thân tại Canada tài trợ:
+ Hồ sơ tài chính của người bảo lãnh.
+ Thư bảo lãnh tài chính (nếu có).

4. GIẤY TỜ TỪ NGƯỜI THÂN TẠI CANADA
- Thư mời thăm thân (Invitation Letter).
- Chứng minh quan hệ:
+ Giấy khai sinh, hình ảnh gia đình, hộ khẩu…
- Giấy tờ cư trú của người mời:
+ PR Card, Study Permit, Work Permit, hoặc Citizenship.
- Nếu người mời tài trợ:
+ Sao kê tài khoản 3–6 tháng.
+ Giấy tờ chứng minh thu nhập: Notice of Assessment (NOA), T4, bảng lương, hợp đồng lao động.

5. GIẤY TỜ CHUYẾN ĐI
- Lịch trình thăm thân.
- Booking khách sạn hoặc giấy xác nhận nơi ở.
- Vé máy bay dự kiến (không bắt buộc).

6. THƯ GIẢI TRÌNH
- Nêu rõ lý do thăm thân.
- Thời gian dự kiến lưu trú.
- Mối quan hệ giữa đôi bên.
- Cam kết quay về Việt Nam.

7. HỒ SƠ DÀNH CHO TRẺ EM (NẾU CÓ)
- Giấy khai sinh bản sao.
- Hộ chiếu riêng của trẻ.
- Giấy xác nhận đang học.
- Nếu trẻ không đi cùng cha và mẹ:
+ Giấy chấp thuận cho trẻ xuất cảnh có xác nhận.
- Hồ sơ tài chính dựa theo cha/mẹ.

8. LƯU Ý QUAN TRỌNG
- Hồ sơ thăm thân Canada cần chứng minh **mối quan hệ thật và hợp pháp**.
- Người mời tại Canada phải có giấy tờ cư trú rõ ràng, hợp lệ.
- Không nên ghi thời gian lưu trú quá dài nếu tài chính không tương xứng.
- Lãnh sự có thể yêu cầu bổ sung hồ sơ hoặc gọi xác minh.
- Hồ sơ rõ ràng, logic và trung thực sẽ giúp tăng tỷ lệ đậu.
"""

        # 4. Create RequiredDocument
        RequiredDocument.objects.get_or_create(
            country=country,
            visa_type=visa_type,
            name="Yêu cầu hồ sơ Visa Thăm thân Canada",
            defaults={"description": description_text},
        )

        self.stdout.write(self.style.SUCCESS("✔ Seed Visa Thăm thân Canada (format chuẩn) thành công!"))

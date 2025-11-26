from django.core.management.base import BaseCommand
from django.utils.text import slugify
from apps.visa.models import Country, VisaType, RequiredDocument


class Command(BaseCommand):
    help = "Seed dữ liệu: Yêu cầu hồ sơ Visa Thăm thân Hoa Kỳ"

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
        visa_type_name = "Visa Thăm thân Hoa Kỳ"
        visa_type, _ = VisaType.objects.get_or_create(
            country=country,
            name=visa_type_name,
            defaults={
                "description": "Visa B2 dùng cho mục đích thăm thân, thăm gia đình, bạn bè đang sinh sống, làm việc hoặc học tập tại Hoa Kỳ.",
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
- Giấy khai sinh (để chứng minh quan hệ gia đình – rất quan trọng).
- Ảnh 5x5 cm nền trắng đúng chuẩn Mỹ.
- Giấy đăng ký kết hôn hoặc độc thân (nếu có yêu cầu).
- Form DS-160 khai trực tuyến (bắt buộc).

2. HỒ SƠ CÔNG VIỆC
**Đối với nhân viên**
- Hợp đồng lao động.
- Xác nhận công việc.
- Đơn xin nghỉ phép thăm thân.
- Bảng lương 3–6 tháng.

**Đối với chủ doanh nghiệp**
- Giấy phép kinh doanh.
- Sao kê tài khoản doanh nghiệp.
- Tài liệu chứng minh hoạt động kinh doanh.

**Đối với lao động tự do**
- Giấy tờ chứng minh công việc thực tế.
- Sao kê tài khoản ngân hàng.

**Đối với học sinh – sinh viên**
- Giấy xác nhận đang học.
- Thẻ học sinh/sinh viên.

3. CHỨNG MINH TÀI CHÍNH
- Sao kê ngân hàng 3–6 tháng.
- Sổ tiết kiệm.
- Tài sản sở hữu: sổ đỏ, ô tô, tài sản có giá trị.
- Chứng minh thu nhập ổn định.
- Nếu người thân bảo lãnh tài chính:
+ Tài chính của người mời: sao kê tài khoản, NOA, W2, paystub.
+ Thư cam kết hỗ trợ tài chính (I-134 – nếu cần).

4. GIẤY TỜ TỪ NGƯỜI THÂN TẠI HOA KỲ
- Thư mời thăm thân (Invitation Letter) ghi rõ:
+ Quan hệ gia đình.
+ Thời gian dự kiến ở lại.
+ Thông tin người mời.
- Chứng minh quan hệ:
+ Giấy khai sinh, hình ảnh gia đình, hộ khẩu…
- Giấy tờ cư trú của người mời:
+ Thẻ xanh (Green Card), Visa Work/Study hợp lệ, hoặc Quốc tịch Mỹ.
- Nếu người mời tài trợ tài chính:
+ Sao kê tài khoản 3–6 tháng.
+ Thuế thu nhập cá nhân (NOA, W2, 1040).
+ Paystub 3 tháng.

5. GIẤY TỜ CHUYẾN ĐI
- Lịch trình thăm thân tại Hoa Kỳ.
- Booking khách sạn (nếu không ở nhà người thân).
- Vé máy bay dự kiến (không bắt buộc).
- Bảo hiểm du lịch (tùy chọn).

6. HỒ SƠ CHO TRẺ EM
- Giấy khai sinh bản sao.
- Hộ chiếu riêng.
- Giấy xác nhận học sinh.
- Giấy đồng ý cho trẻ xuất cảnh của cha/mẹ (nếu chỉ 1 người đi cùng).

7. THƯ GIẢI TRÌNH (NẾU CẦN)
- Lý do thăm thân.
- Dự kiến thời gian lưu trú.
- Cam kết quay về Việt Nam.

8. LƯU Ý QUAN TRỌNG
- Hồ sơ Mỹ tập trung chính vào **phỏng vấn**, không nộp hồ sơ giấy trước.
- Cần chứng minh ràng buộc mạnh ở Việt Nam: tài chính, công việc, gia đình.
- Không chuẩn bị hồ sơ giả hoặc thông tin sai lệch.
- Lãnh sự có thể yêu cầu xem hồ sơ bổ sung trong buổi phỏng vấn.
"""

        # 4. Create RequiredDocument
        RequiredDocument.objects.get_or_create(
            country=country,
            visa_type=visa_type,
            name="Yêu cầu hồ sơ Visa Thăm thân Hoa Kỳ",
            defaults={"description": description_text},
        )

        self.stdout.write(self.style.SUCCESS("✔ Seed Visa Thăm thân Hoa Kỳ (format chuẩn) thành công!"))

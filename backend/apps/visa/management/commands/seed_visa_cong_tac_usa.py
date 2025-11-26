from django.core.management.base import BaseCommand
from django.utils.text import slugify
from apps.visa.models import Country, VisaType, RequiredDocument


class Command(BaseCommand):
    help = "Seed dữ liệu: Yêu cầu hồ sơ Visa Công tác Hoa Kỳ"

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
        visa_type_name = "Visa Công tác Hoa Kỳ"
        visa_type, _ = VisaType.objects.get_or_create(
            country=country,
            name=visa_type_name,
            defaults={
                "description": "Visa B1 dùng cho mục đích công tác, tham dự hội nghị, họp đối tác, ký kết hợp đồng hoặc tham gia các hoạt động thương mại tại Hoa Kỳ.",
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
- Ảnh 5x5 cm nền trắng (chuẩn visa Mỹ).
- Giấy đăng ký kết hôn (nếu đã kết hôn).
- Form DS-160 khai trực tuyến.

2. HỒ SƠ CÔNG VIỆC
**Đối với nhân viên**
- Hợp đồng lao động.
- Xác nhận công việc và mức lương.
- Quyết định cử đi công tác (nêu rõ thời gian & mục đích).
- Bảng lương 3–6 tháng gần nhất.

**Đối với chủ doanh nghiệp**
- Giấy phép kinh doanh.
- Báo cáo thuế hoặc báo cáo tài chính (nếu có).
- Sao kê tài khoản doanh nghiệp.
- Tài liệu chứng minh hoạt động kinh doanh.

**Đối với người làm tự do**
- Giấy tờ chứng minh công việc thực tế.
- Sao kê ngân hàng.

3. CHỨNG MINH TÀI CHÍNH
- Sao kê ngân hàng cá nhân 3–6 tháng.
- Sổ tiết kiệm (nếu có).
- Tài sản sở hữu: bất động sản, ô tô, tài sản giá trị.
- Nếu công ty tài trợ chi phí:
+ Thư bảo lãnh chi trả chi phí công tác.
+ Sao kê tài khoản công ty.
+ Báo cáo thuế / báo cáo tài chính.

4. GIẤY TỜ CÔNG TÁC TỪ HOA KỲ
- Thư mời công tác (Invitation Letter) từ đối tác Mỹ:
+ Nêu rõ mục đích, thời gian, địa điểm.
+ Người liên hệ tại Hoa Kỳ.
- Các giấy tờ chứng minh quan hệ hợp tác:
+ Hợp đồng, MOU, email trao đổi, lịch họp.
- Giấy tờ công ty tại Hoa Kỳ (nếu có):
+ Business license, website, danh thiếp, thông tin doanh nghiệp.

5. GIẤY TỜ CHUYẾN ĐI
- Lịch trình công tác chi tiết.
- Booking khách sạn hoặc xác nhận nơi lưu trú.
- Vé máy bay dự kiến (không bắt buộc).
- Bảo hiểm du lịch quốc tế (tùy chọn).

6. THƯ GIẢI TRÌNH
- Mục đích chuyến công tác.
- Vai trò của ứng viên trong công ty.
- Cam kết quay lại Việt Nam sau công tác.

7. LƯU Ý QUAN TRỌNG
- Visa công tác Hoa Kỳ không yêu cầu nộp hồ sơ giấy trước buổi phỏng vấn.
- Kết quả visa phụ thuộc nhiều vào sự nhất quán khi phỏng vấn.
- Cần chứng minh ràng buộc mạnh: công việc, thu nhập, tài sản.
- Mọi giấy tờ nên rõ ràng, trung thực và dễ đối chiếu khi LSQ yêu cầu.
- Lãnh sự có thể yêu cầu chứng cứ hợp tác giữa hai công ty.
"""

        # 4. Create RequiredDocument
        RequiredDocument.objects.get_or_create(
            country=country,
            visa_type=visa_type,
            name="Yêu cầu hồ sơ Visa Công tác Hoa Kỳ",
            defaults={"description": description_text},
        )

        self.stdout.write(self.style.SUCCESS("✔ Seed Visa Công tác Hoa Kỳ (format chuẩn) thành công!"))

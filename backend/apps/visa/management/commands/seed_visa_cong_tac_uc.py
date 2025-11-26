from django.core.management.base import BaseCommand
from django.utils.text import slugify
from apps.visa.models import Country, VisaType, RequiredDocument


class Command(BaseCommand):
    help = "Seed dữ liệu: Yêu cầu hồ sơ Visa Công tác Úc"

    def handle(self, *args, **options):
        # 1. Country
        country_name = "Úc"
        country, _ = Country.objects.get_or_create(
            name=country_name,
            defaults={
                "code": "AU",
                "region": "Châu Đại Dương",
                "slug": slugify(country_name),
            },
        )

        # 2. VisaType
        visa_type_name = "Visa Công tác Úc"
        visa_type, _ = VisaType.objects.get_or_create(
            country=country,
            name=visa_type_name,
            defaults={
                "description": "Visa dành cho mục đích hội họp, làm việc ngắn hạn tại Úc.",
                "purpose": "business",
                "slug": slugify(visa_type_name),
            },
        )

        # 3. DESCRIPTION FORMAT (giống 100% format bạn yêu cầu)
        description_text = """
1. HỒ SƠ NHÂN THÂN
- Hộ chiếu còn hạn ít nhất 6 tháng.
- CCCD/CMND.
- Sổ hộ khẩu (bản sao).
- Giấy khai sinh (nếu đi theo gia đình).
- Giấy đăng ký kết hôn (nếu đã kết hôn).
- Ảnh 4x6 nền trắng (tùy thời điểm yêu cầu).

2. HỒ SƠ CÔNG VIỆC
**Đối với nhân viên**
- Hợp đồng lao động.
- Bảng lương 3–6 tháng.
- Xác nhận công việc ghi rõ chức vụ.
- Quyết định cử đi công tác của công ty.
- Lịch công tác tại Úc (nếu có).

**Đối với chủ doanh nghiệp**
- Giấy phép kinh doanh.
- Sao kê tài khoản doanh nghiệp 3–6 tháng.
- Hồ sơ thuế (nếu có).

**Đối với lao động tự do**
- Tài liệu chứng minh nguồn thu nhập thực tế.

3. CHỨNG MINH TÀI CHÍNH
- Sao kê ngân hàng 3–6 tháng.
- Sổ tiết kiệm (nếu có).
- Chứng minh tài sản: nhà đất, xe cộ…
- Chứng minh ràng buộc tại Việt Nam: công việc, gia đình, tài sản.

4. THƯ MỜI CÔNG TÁC TỪ ÚC
- Thư mời công tác, ghi rõ mục đích, thời gian làm việc.
- Thông tin công ty phía Úc: địa chỉ, liên hệ, ABN (nếu có).
- Nếu phía Úc tài trợ chi phí:
+ Xác nhận tài trợ.
+ Sao kê ngân hàng/thu nhập của công ty mời.

5. GIẤY TỜ DOANH NGHIỆP TẠI VIỆT NAM (nếu đi với tư cách đại diện công ty)
- Hồ sơ pháp lý doanh nghiệp.
- Giới thiệu công ty, hợp tác giữa 2 bên (nếu có).
- Tài liệu chứng minh quan hệ công việc với phía Úc.

6. GIẤY TỜ CHUYẾN ĐI
- Lịch trình công tác tại Úc.
- Booking khách sạn.
- Vé máy bay dự kiến (không bắt buộc xuất vé).
- Bảo hiểm du lịch/công tác (khuyến nghị).

7. HỒ SƠ DÀNH CHO TRẺ EM (NẾU ĐI CÙNG)
- Giấy khai sinh.
- Hộ chiếu của trẻ.
- Giấy xác nhận đang học tại trường.
- Nếu trẻ không đi cùng cả cha và mẹ:
+ Giấy đồng ý ủy quyền có xác nhận.
- Công việc và tài chính sẽ dựa theo hồ sơ cha/mẹ.

8. LƯU Ý QUAN TRỌNG
- Hồ sơ công tác cần **chứng minh rõ mục đích làm việc – mối quan hệ giữa hai công ty**.
- Thư mời phải thể hiện thông tin chính xác và kiểm chứng được.
- Không nên ghi thời gian lưu trú quá dài so với lịch công tác.
- Lãnh sự Úc có thể yêu cầu bổ sung hồ sơ hoặc gọi xác minh.
- Hồ sơ rõ ràng – trung thực – logic sẽ tăng tỷ lệ đậu.
"""

        # 4. Seed RequiredDocument
        RequiredDocument.objects.get_or_create(
            country=country,
            visa_type=visa_type,
            name="Yêu cầu hồ sơ Visa Công tác Úc",
            defaults={"description": description_text},
        )

        self.stdout.write(self.style.SUCCESS("✔ Seed Visa Công tác Úc (format chuẩn) thành công!"))

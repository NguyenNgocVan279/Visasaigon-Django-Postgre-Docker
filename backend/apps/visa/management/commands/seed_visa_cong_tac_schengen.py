from django.core.management.base import BaseCommand
from django.utils.text import slugify
from apps.visa.models import Country, VisaType, RequiredDocument


class Command(BaseCommand):
    help = "Seed dữ liệu: Yêu cầu hồ sơ Visa Công tác Schengen"

    def handle(self, *args, **options):
        # 1. Country
        country_name = "Khối Schengen"
        country, _ = Country.objects.get_or_create(
            name=country_name,
            defaults={
                "code": "SCH",
                "region": "Châu Âu",
                "slug": slugify(country_name),
            },
        )

        # 2. VisaType
        visa_type_name = "Visa Công tác Schengen"
        visa_type, _ = VisaType.objects.get_or_create(
            country=country,
            name=visa_type_name,
            defaults={
                "description": "Visa Schengen công tác (Business Visa) dùng để tham dự hội nghị, họp đối tác, ký kết hợp đồng hoặc tham gia các hoạt động thương mại tại các quốc gia thuộc khối Schengen.",
                "purpose": "business",
                "slug": slugify(visa_type_name),
            },
        )

        # 3. DESCRIPTION FORMAT
        description_text = """
1. HỒ SƠ NHÂN THÂN
- Hộ chiếu còn hạn tối thiểu 3–6 tháng sau ngày dự kiến rời Schengen.
- Hộ chiếu cũ (nếu đã từng đi nước ngoài).
- CCCD/CMND.
- Sổ hộ khẩu (bản sao công chứng).
- Ảnh 3.5x4.5cm nền trắng (chuẩn Schengen).
- Giấy đăng ký kết hôn / ly hôn (nếu có).
- Tờ khai Schengen form (điền đầy đủ & ký tên).

2. HỒ SƠ CÔNG VIỆC
**Đối với nhân viên**
- Hợp đồng lao động.
- Bảng lương 3–6 tháng.
- Xác nhận công tác, nêu rõ chức vụ, thời gian làm việc.
- Quyết định cử đi công tác từ công ty Việt Nam.

**Đối với chủ doanh nghiệp**
- Giấy phép kinh doanh.
- Sao kê tài khoản doanh nghiệp 3–6 tháng.
- Báo cáo thuế năm gần nhất (nếu có).

**Đối với người làm tự do**
- Giấy tờ chứng minh nguồn thu nhập: hợp đồng dịch vụ, giấy phép hành nghề.
- Sao kê tài khoản ngân hàng.

3. CHỨNG MINH TÀI CHÍNH
- Sổ tiết kiệm hoặc sao kê ngân hàng 3–6 tháng.
- Tài sản sở hữu: sổ đỏ, xe ô tô, hoặc tài sản khác.
- Thu nhập ổn định & đủ tài chính cho chuyến đi.
- Nếu công ty chi trả toàn bộ:
+ Thư bảo lãnh tài chính.
+ Hồ sơ tài chính của công ty.

4. GIẤY TỜ CÔNG TÁC TỪ CÔNG TY PHÍA SCHENGEN
- Thư mời (Invitation Letter) từ công ty/đối tác tại Schengen:
+ Thông tin công ty mời.
+ Thông tin ứng viên.
+ Mục đích công tác.
+ Thời gian – địa điểm công tác.
+ Ai chịu chi phí chuyến đi.
- Giấy chứng nhận đăng ký kinh doanh của công ty tại Schengen (nếu có).
- Lịch trình cuộc họp / hội nghị / triển lãm.
- Bằng chứng quan hệ hợp tác:
+ Email trao đổi.
+ Hợp đồng / MOU.
+ Vé tham dự hội nghị (nếu công tác theo sự kiện).

5. GIẤY TỜ CHUYẾN ĐI
- Booking khách sạn hoặc giấy xác nhận nơi lưu trú.
- Vé máy bay khứ hồi (có thể là vé dự kiến).
- Lịch trình công tác chi tiết tại các quốc gia Schengen.
- Nếu di chuyển giữa nhiều nước:
+ Lịch trình di chuyển và xác nhận phương tiện.

6. BẢO HIỂM DU LỊCH SCHENGEN
- Bảo hiểm du lịch quốc tế **tối thiểu 30.000 EUR**.
- Hiệu lực trong toàn bộ thời gian lưu trú tại Schengen.
- Hiệu lực tại toàn bộ 27 quốc gia Schengen.

7. THƯ GIẢI TRÌNH
- Nêu rõ mục đích công tác.
- Tầm quan trọng của việc đi công tác đối với công ty.
- Ràng buộc quay về Việt Nam.

8. LƯU Ý QUAN TRỌNG
- Nộp hồ sơ cho nước **đến đầu tiên** hoặc **lưu trú lâu nhất** trong hành trình.
- Hồ sơ phải thống nhất giữa:
+ Công ty Việt Nam.
+ Công ty/đối tác Schengen.
+ Vé máy bay và lịch trình.
- Một số nước Schengen yêu cầu tới phỏng vấn trực tiếp.
- Cần chứng minh ràng buộc mạnh tại Việt Nam: công việc, thu nhập, tài sản.
- Thư mời nên có đóng dấu và chữ ký của người đại diện hợp pháp.
"""

        # 4. Create RequiredDocument
        RequiredDocument.objects.get_or_create(
            country=country,
            visa_type=visa_type,
            name="Yêu cầu hồ sơ Visa Công tác Schengen",
            defaults={"description": description_text},
        )

        self.stdout.write(self.style.SUCCESS("✔ Seed Visa Công tác Schengen (format chuẩn) thành công!"))

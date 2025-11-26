from django.core.management.base import BaseCommand
from django.utils.text import slugify
from apps.visa.models import Country, VisaType, RequiredDocument


class Command(BaseCommand):
    help = "Seed dữ liệu: Yêu cầu hồ sơ Visa Du lịch Schengen"

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
        visa_type_name = "Visa Du lịch Schengen"
        visa_type, _ = VisaType.objects.get_or_create(
            country=country,
            name=visa_type_name,
            defaults={
                "description": "Visa Schengen du lịch dành cho mục đích thăm quan, nghỉ dưỡng hoặc khám phá các quốc gia thuộc khối Schengen.",
                "purpose": "tourist",
                "slug": slugify(visa_type_name),
            },
        )

        # 3. DESCRIPTION FORMAT
        description_text = """
1. HỒ SƠ NHÂN THÂN
- Hộ chiếu còn hạn ít nhất 3–6 tháng sau ngày rời Schengen.
- Hộ chiếu cũ (nếu có).
- CCCD/CMND.
- Sổ hộ khẩu (bản sao công chứng).
- Ảnh 3.5x4.5cm nền trắng đúng chuẩn Schengen.
- Giấy đăng ký kết hôn / ly hôn (nếu có).
- Tờ khai xin visa Schengen (điền đầy đủ và ký tên).

2. HỒ SƠ CÔNG VIỆC
**Đối với nhân viên**
- Hợp đồng lao động.
- Xác nhận công việc.
- Đơn xin nghỉ phép du lịch.
- Bảng lương 3–6 tháng gần nhất.

**Đối với chủ doanh nghiệp**
- Giấy phép kinh doanh.
- Sao kê tài khoản doanh nghiệp 3–6 tháng.
- Báo cáo thuế hoặc báo cáo tài chính (nếu có).

**Đối với lao động tự do**
- Giấy tờ chứng minh nguồn thu nhập thực tế.
- Sao kê ngân hàng.

**Đối với học sinh – sinh viên**
- Giấy xác nhận đang học.
- Thẻ học sinh/sinh viên.

3. CHỨNG MINH TÀI CHÍNH
- Sổ tiết kiệm (khuyến khích ≥ 100 triệu tùy thời gian lưu trú).
- Sao kê ngân hàng cá nhân 3–6 tháng.
- Chứng minh thu nhập ổn định.
- Tài sản sở hữu: nhà đất, ô tô, tài sản giá trị.
- Nếu có người tài trợ:
+ Thư bảo lãnh tài chính.
+ Tài chính của người bảo lãnh.

4. HỒ SƠ DU LỊCH
- **Lịch trình chi tiết** (ngày – giờ – các điểm tham quan).
- Booking khách sạn đầy đủ cho toàn bộ thời gian lưu trú.
- Booking vé máy bay khứ hồi (có thể là vé dự kiến).
- Booking di chuyển nội địa (nếu đi nhiều quốc gia).
- Nếu đi theo tour: hợp đồng tour + giấy xác nhận dịch vụ.

5. BẢO HIỂM DU LỊCH SCHENGEN
- Bảo hiểm du lịch quốc tế tối thiểu **30.000 EUR**.
- Có hiệu lực tại toàn bộ **27 quốc gia Schengen**.
- Có hiệu lực cho toàn bộ thời gian lưu trú.

6. HỒ SƠ THĂM THÂN (NẾU Ở NHÀ NGƯỜI THÂN / BẠN BÈ)
- Thư mời (Invitation Letter).
- Giấy tờ cư trú của người mời:
+ Thẻ cư trú, hộ chiếu EU, visa dài hạn.
- Chứng minh quan hệ:
+ Giấy khai sinh, hình ảnh, liên lạc, giấy tờ tương ứng.
- Giấy xác nhận nơi ở (Wohnungsgeberbestätigung – nếu Đức).
- Tài chính của người mời (nếu tài trợ):
+ Sao kê ngân hàng 3–6 tháng.
+ Giấy chứng nhận bảo lãnh tài chính: Form Verpflichtungserklärung (ở Đức) hoặc tương đương ở các nước khác.

7. HỒ SƠ CHO TRẺ EM (NẾU ĐI CÙNG)
- Giấy khai sinh.
- Giấy ủy quyền của cha/mẹ nếu chỉ một phụ huynh đi.
- Hộ chiếu riêng.
- Giấy xác nhận đang học.

8. THƯ GIẢI TRÌNH (NẾU CẦN)
- Lý do du lịch.
- Thời gian dự kiến lưu trú.
- Ràng buộc quay về Việt Nam sau chuyến đi.

9. LƯU Ý QUAN TRỌNG
- Nộp đơn tại quốc gia Schengen:
+ Đến đầu tiên **hoặc**
+ Lưu trú lâu nhất trong hành trình.
- Hồ sơ cần sự nhất quán giữa:
+ lịch trình – booking – tài chính – giấy tờ cá nhân.
- Một số nước yêu cầu phỏng vấn trực tiếp (Đức, Áo, Hà Lan…).
- Không dùng tài khoản mới mở hoặc không có giao dịch thực tế.
- Thông tin phải trung thực, rõ ràng và dễ kiểm chứng.
"""

        # 4. Create RequiredDocument
        RequiredDocument.objects.get_or_create(
            country=country,
            visa_type=visa_type,
            name="Yêu cầu hồ sơ Visa Du lịch Schengen",
            defaults={"description": description_text},
        )

        self.stdout.write(self.style.SUCCESS("✔ Seed Visa Du lịch Schengen (format chuẩn) thành công!"))

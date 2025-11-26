from django.core.management.base import BaseCommand
from django.utils.text import slugify
from apps.visa.models import Country, VisaType, RequiredDocument


class Command(BaseCommand):
    help = "Seed dữ liệu: Yêu cầu hồ sơ Visa Thăm thân Schengen"

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
        visa_type_name = "Visa Thăm thân Schengen"
        visa_type, _ = VisaType.objects.get_or_create(
            country=country,
            name=visa_type_name,
            defaults={
                "description": "Visa thăm thân dành cho người có người thân hoặc bạn bè cư trú hợp pháp tại một quốc gia thuộc khối Schengen.",
                "purpose": "family_visit",
                "slug": slugify(visa_type_name),
            },
        )

        # 3. DESCRIPTION FORMAT
        description_text = """
1. HỒ SƠ NHÂN THÂN
- Hộ chiếu còn hạn tối thiểu 3–6 tháng sau ngày rời Schengen.
- Hộ chiếu cũ (nếu có).
- CCCD/CMND.
- Sổ hộ khẩu (bản sao công chứng).
- Ảnh 3.5x4.5cm nền trắng tiêu chuẩn Schengen.
- Tờ khai xin visa (ký tên đầy đủ).
- Giấy đăng ký kết hôn / ly hôn / khai sinh con (nếu có).

2. HỒ SƠ CHỨNG MINH QUAN HỆ
- Giấy tờ chứng minh quan hệ thân nhân:  
  + Khai sinh, sổ hộ khẩu, giấy đăng ký kết hôn, ảnh chụp chung, tin nhắn, lịch sử liên lạc.  
- Đối với bạn bè:  
  + Ảnh chụp chung, lịch sử trò chuyện, email, thư xác nhận quan hệ.  

3. THƯ MỜI THĂM THÂN (INVITATION LETTER)
Thư mời phải bao gồm:
- Thông tin người mời và người được mời.
- Lý do mời và thời gian lưu trú.
- Địa chỉ cư trú tại Schengen.
- Ai chi trả chi phí cho chuyến đi.
- Chữ ký tay của người mời.

4. GIẤY TỜ CỦA NGƯỜI MỜI (BẮT BUỘC)
**Nếu người mời là công dân EU/Schengen**
- Hộ chiếu EU hoặc căn cước công dân.
- Giấy chứng nhận cư trú.

**Nếu người mời là người nước ngoài cư trú tại Schengen**
- Thẻ cư trú (Residence Permit / Aufenthaltstitel).
- Hộ chiếu.

**Các giấy tờ bổ sung**
- Hợp đồng thuê nhà hoặc giấy sở hữu nhà.
- Giấy xác nhận cư trú (Ví dụ: Wohnungsgeberbestätigung – Đức).

5. TÀI CHÍNH CỦA NGƯỜI MỜI (NẾU TÀI TRỢ CHI PHÍ)
- Sao kê ngân hàng 3–6 tháng.
- Giấy chứng nhận việc làm hoặc hợp đồng lao động.
- Giấy xác nhận thu nhập hoặc bảng lương.
- **Giấy bảo lãnh tài chính chính thức của chính phủ** (khuyến khích hoặc bắt buộc ở nhiều nước):
  + Đức: **Verpflichtungserklärung**  
  + Hà Lan: Proof of Sponsorship  
  + Pháp: Attestation d’accueil (bản gốc)  
  + Các nước khác có mẫu tương đương.

6. TÀI CHÍNH NGƯỜI ĐƯỢC MỜI (NẾU TỰ CHI TRẢ)
- Sổ tiết kiệm.
- Sao kê ngân hàng 3–6 tháng.
- Chứng minh thu nhập.
- Tài sản sở hữu (nhà, đất, ô tô…).

7. HỒ SƠ CÔNG VIỆC CỦA NGƯỜI ĐƯỢC MỜI
**Nhân viên**
- Hợp đồng lao động.
- Xác nhận công việc.
- Đơn xin nghỉ phép thăm thân.
- Bảng lương 3–6 tháng.

**Chủ doanh nghiệp**
- Giấy phép kinh doanh.
- Sao kê ngân hàng doanh nghiệp.
- Báo cáo thuế / báo cáo tài chính.

**Lao động tự do**
- Chứng minh thu nhập thực tế.
- Sao kê ngân hàng.

**Học sinh – sinh viên**
- Giấy xác nhận đang học.
- Thẻ học sinh/sinh viên.

8. HỒ SƠ CHO CHUYẾN ĐI
- Lịch trình chi tiết thời gian lưu trú tại quốc gia Schengen.
- Booking vé máy bay khứ hồi (có thể là vé dự kiến).
- Bảo hiểm du lịch trị giá tối thiểu **30.000 EUR**, hiệu lực toàn bộ khối Schengen.
- Nếu không ở nhà người mời: booking khách sạn cho toàn bộ thời gian.

9. HỒ SƠ CHO TRẺ EM (NẾU CÙNG ĐI)
- Giấy khai sinh.
- Hộ chiếu riêng.
- Giấy ủy quyền của cha/mẹ nếu không đi cùng cả hai.
- Giấy xác nhận đang học.

10. THƯ GIẢI TRÌNH (NẾU CẦN)
- Lý do thăm thân.
- Mối quan hệ với người mời.
- Khả năng tài chính và ràng buộc quay lại Việt Nam.

11. LƯU Ý QUAN TRỌNG
- Quốc gia nộp đơn phải là nước:
  + lưu trú lâu nhất **hoặc**  
  + quốc gia đến đầu tiên.  
- Thông tin về quan hệ phải rõ ràng và dễ chứng minh.
- Nhiều quốc gia yêu cầu phỏng vấn trực tiếp (Đức, Hà Lan, Thụy Điển…).
- Thông tin giữa thư mời – lịch trình – tài chính phải thống nhất.
"""

        # 4. Create RequiredDocument
        RequiredDocument.objects.get_or_create(
            country=country,
            visa_type=visa_type,
            name="Yêu cầu hồ sơ Visa Thăm thân Schengen",
            defaults={"description": description_text},
        )

        self.stdout.write(self.style.SUCCESS("✔ Seed Visa Thăm thân Schengen thành công!"))

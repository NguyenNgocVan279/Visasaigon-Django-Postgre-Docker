from django.core.management.base import BaseCommand
from django.utils.text import slugify

from apps.visa.models import Country, VisaType, RequiredDocument


DESCRIPTION_FAMILY_AU = """
1. HỒ SƠ NHÂN THÂN
- Hộ chiếu còn hạn ít nhất 6 tháng.
- CCCD/CMND.
- Sổ hộ khẩu (bản sao).
- Giấy khai sinh (để chứng minh quan hệ gia đình).
- Giấy đăng ký kết hôn (nếu đã kết hôn).
- Ảnh 4x6 nền trắng (tùy thời điểm yêu cầu).

2. HỒ SƠ CÔNG VIỆC
**Đối với nhân viên**
- Hợp đồng lao động.
- Bảng lương 3–6 tháng.
- Xác nhận công việc.
- Đơn xin nghỉ phép để đi thăm thân.

**Đối với chủ doanh nghiệp**
- Giấy phép kinh doanh.
- Sao kê tài khoản doanh nghiệp 3–6 tháng.

**Đối với lao động tự do**
- Tài liệu chứng minh thu nhập thực tế.

**Đối với học sinh – sinh viên**
- Giấy xác nhận đang học.
- Thẻ học sinh/sinh viên.

3. CHỨNG MINH TÀI CHÍNH
- Sổ tiết kiệm hoặc sao kê ngân hàng 3–6 tháng.
- Chứng minh thu nhập ổn định.
- Giấy tờ nhà đất, xe cộ…
- Chứng minh ràng buộc tại Việt Nam: công việc, gia đình, tài sản.

4. GIẤY TỜ TỪ NGƯỜI THÂN TẠI ÚC
- Thư mời thăm thân (Invitation Letter).
- Chứng minh quan hệ:  
  + Giấy khai sinh, sổ hộ khẩu, hình ảnh gia đình…
- Tài liệu cư trú của người mời:
  + Passport Úc / Visa Úc / PR / Citizenship Certificate.
- Nếu người mời bảo trợ tài chính:
  + Sao kê tài khoản 3–6 tháng.
  + Giấy tờ chứng minh thu nhập.
  + Form chứng minh bảo trợ (nếu có yêu cầu tùy hồ sơ).

5. GIẤY TỜ CHUYẾN ĐI
- Lịch trình thăm thân tại Úc.
- Booking khách sạn hoặc giấy xác nhận nơi ở với người thân.
- Vé máy bay dự kiến (không bắt buộc mua).

6. HỒ SƠ DÀNH CHO TRẺ EM
- Giấy khai sinh.
- Hộ chiếu riêng của trẻ.
- Giấy xác nhận đang học tại trường.
- Khi trẻ không đi cùng cả cha và mẹ:
  + Giấy đồng ý cho trẻ đi nước ngoài có xác nhận.
- Tài chính và công việc sẽ dựa theo hồ sơ cha/mẹ.

7. LƯU Ý QUAN TRỌNG
- Hồ sơ thăm thân Úc cần chứng minh **mối quan hệ thật – chính xác – có bằng chứng**.
- Nếu người thân tại Úc tài trợ tài chính, cần chứng minh năng lực chi trả.
- Không nên ghi thời gian lưu trú quá dài so với công việc/tài chính tại Việt Nam.
- Lãnh sự Úc có thể yêu cầu bổ sung hồ sơ hoặc gọi xác minh.
- Hồ sơ càng rõ ràng – logic – dễ hiểu thì tỷ lệ đậu càng cao.
""".strip()


class Command(BaseCommand):
    help = "Seed data: Yêu cầu hồ sơ Visa Thăm thân Úc (full description)"

    def handle(self, *args, **kwargs):
        # 1. Country Úc
        country_name = "Úc"
        country, _ = Country.objects.get_or_create(
            name=country_name,
            defaults={
                "code": "AU",
                "region": "Châu Đại Dương",
                "slug": slugify(country_name)
            }
        )

        # 2. VisaType: Thăm thân
        visa_name = "Visa Thăm thân Úc"
        visa_type, _ = VisaType.objects.get_or_create(
            country=country,
            purpose="family_visit",
            name=visa_name,
            defaults={
                "description": "Visa thăm thân Úc dành cho người muốn sang thăm gia đình, họ hàng.",
                "slug": slugify(visa_name)
            }
        )

        # 3. RequiredDocument – một dòng duy nhất
        doc_name = "Yêu cầu hồ sơ visa Thăm thân Úc"

        RequiredDocument.objects.update_or_create(
            country=country,
            visa_type=visa_type,
            name=doc_name,
            defaults={"description": DESCRIPTION_FAMILY_AU}
        )

        self.stdout.write(self.style.SUCCESS("Seed thành công: Visa Thăm thân Úc"))

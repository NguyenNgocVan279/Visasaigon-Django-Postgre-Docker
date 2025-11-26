from django.core.management.base import BaseCommand
from django.utils.text import slugify

from apps.visa.models import Country, VisaType, RequiredDocument


DESCRIPTION_TOURISM_AU = """
1. HỒ SƠ NHÂN THÂN
- Hộ chiếu còn hạn ít nhất 6 tháng.
- CCCD/CMND.
- Sổ hộ khẩu (bản sao).
- Giấy khai sinh (nếu đi cùng trẻ em).
- Giấy đăng ký kết hôn (nếu đã kết hôn).
- Ảnh 4x6 nền trắng (tùy từng thời điểm yêu cầu).

2. HỒ SƠ CÔNG VIỆC
**Đối với nhân viên**
- Hợp đồng lao động.
- Xác nhận công việc.
- Bảng lương 3–6 tháng.
- Đơn xin nghỉ phép.

**Đối với chủ doanh nghiệp**
- Giấy phép kinh doanh.
- Sao kê tài khoản doanh nghiệp 3–6 tháng.

**Đối với lao động tự do**
- Các bằng chứng chứng minh thu nhập thực tế.

**Đối với học sinh – sinh viên**
- Giấy xác nhận đang học.
- Thẻ học sinh/sinh viên.

3. CHỨNG MINH TÀI CHÍNH
- Sổ tiết kiệm hoặc sao kê ngân hàng 3–6 tháng.
- Chứng minh thu nhập hàng tháng.
- Giấy tờ tài sản (nhà đất, xe cộ…).
- Chứng minh ràng buộc tại Việt Nam: gia đình, công việc, tài sản.

4. GIẤY TỜ CHUYẾN ĐI
- Lịch trình du lịch tại Úc.
- Booking khách sạn (nếu có).
- Vé máy bay dự kiến (không bắt buộc mua trước).
- Nếu có người mời:
  + Thư mời.
  + Bằng chứng quan hệ.
  + Tài liệu cư trú hoặc quốc tịch của người mời.

5. HỒ SƠ DÀNH CHO TRẺ EM
- Giấy khai sinh.
- Hộ chiếu riêng của trẻ.
- Giấy xác nhận đang học.
- Nếu trẻ không đi cùng cả cha và mẹ: 
  + Giấy uỷ quyền/đồng ý cho trẻ đi nước ngoài có xác nhận.
- Tài chính sẽ dùng hồ sơ của cha mẹ.

6. LƯU Ý QUAN TRỌNG
- Úc yêu cầu nộp hồ sơ rất đầy đủ và chi tiết.
- Hồ sơ tài chính mạnh giúp tăng tỷ lệ đậu.
- Không nên làm lịch trình quá dài nếu tài chính và thời gian nghỉ phép không phù hợp.
- Lãnh sự Úc có thể yêu cầu bổ sung hồ sơ bất kỳ lúc nào.
- Nên đảm bảo tính logic giữa tài chính – công việc – mục đích chuyến đi.
""".strip()


class Command(BaseCommand):
    help = "Seed data: Yêu cầu hồ sơ Visa Du lịch Úc (full description)"

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

        # 2. VisaType: Du lịch
        visa_name = "Visa Du lịch Úc"
        visa_type, _ = VisaType.objects.get_or_create(
            country=country,
            purpose="tourism",
            name=visa_name,
            defaults={
                "description": "Visa du lịch Úc dành cho khách muốn tham quan, nghỉ dưỡng.",
                "slug": slugify(visa_name)
            }
        )

        # 3. RequiredDocument – một dòng duy nhất
        doc_name = f"Yêu cầu hồ sơ visa Du lịch Úc"

        RequiredDocument.objects.update_or_create(
            country=country,
            visa_type=visa_type,
            name=doc_name,
            defaults={"description": DESCRIPTION_TOURISM_AU}
        )

        self.stdout.write(self.style.SUCCESS("Seed thành công: Visa Du lịch Úc"))

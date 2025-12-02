from django.core.management.base import BaseCommand
from apps.visa.models import Country, CountryDetail, CountrySection, CountryTip
from apps.faq.models import FAQItem, FAQCategory

class Command(BaseCommand):
    help = 'Seed data cho bảng CountryDetail, Section, Tip, FAQ'

    def handle(self, *args, **options):
        country_slugs = ["uc", "canada", "hoa-ky", "khoi-schengen"]
        countries = {c.slug: c for c in Country.objects.filter(slug__in=country_slugs)}

        # COUNTRY DETAIL
        detail_data = {
            "uc": {
                "hero_title": "Visa Úc – Hướng dẫn cập nhật mới nhất (2025)",
                "hero_subtitle": "Tìm hiểu quy trình, giấy tờ và lưu ý quan trọng khi xin visa Úc.",
                "overview_title": "Tổng quan Visa Úc",
                "overview_content": "Visa Úc là giấy phép do Chính phủ Úc cấp, cho phép công dân nước ngoài nhập cảnh để du lịch, thăm thân, công tác hoặc học tập tùy theo mục đích. Mỗi loại visa có điều kiện, thời hạn lưu trú và quy trình xét duyệt khác nhau. Hiểu rõ từng loại visa giúp hồ sơ của bạn phù hợp yêu cầu và tăng khả năng đậu ngay từ lần nộp đầu tiên.",
                "visa_types_summary": "Du lịch, thăm thân, công tác",
                "visa_processing_time": "Lưu ý nổi bật:",
                "visa_highlight_note_1": "Hồ sơ đầy đủ, chính xác và trung thực",
                "visa_highlight_note_2": "Sinh trắc học (biometrics) & y tế.",
                "visa_highlight_note_3": "Chứng minh tài chính & ràng buộc về mục đích.",
                "cta_featured_requirement_1": "Hộ chiếu hợp lệ.",
                "cta_featured_requirement_2": "Chứng minh tài chính.",
                "cta_featured_requirement_3": "Chứng minh công việc / ràng buộc tại Việt Nam.",
                "cta_featured_requirement_4": "Lịch sử du lịch & giấy tờ nhân thân.",
                "cta_subtitle": "Tra cứu chi tiết yêu cầu hồ sơ",
                "cta_button_text": "Tra cứu yêu cầu hồ sơ",
                "cta_button_link": "/visa/ho-so-yeu-cau/",
            },
            "canada": {
                "hero_title": "Visa Canada – Quy trình & yêu cầu mới nhất",
                "hero_subtitle": "Hướng dẫn chuẩn bị hồ sơ và chứng minh tài chính khi xin visa Canada.",
                "overview_title": "Tổng quan Visa Canada",
                "overview_content": (
                    "Visa du lịch Canada yêu cầu lịch trình rõ ràng, tài chính mạnh, và bằng chứng ràng buộc tại Việt Nam như công việc, tài sản."
                ),
                "visa_types_summary": "Du lịch, thăm thân, công tác",
                "visa_processing_time": "15–45 ngày làm việc",
                "visa_highlight_note_1": "Tài chính minh bạch và ổn định.",
                "visa_highlight_note_2": "Lịch trình du lịch chi tiết.",
                "visa_highlight_note_3": "Chứng minh ràng buộc mạnh tại Việt Nam.",
                "cta_title": "Chuẩn bị hồ sơ visa Canada",
                "cta_featured_requirement_1": "Hộ chiếu còn hạn 6 tháng.",
                "cta_featured_requirement_2": "Sao kê ngân hàng, bảng lương.",
                "cta_featured_requirement_3": "Giấy tờ công việc hoặc tài sản.",
                "cta_featured_requirement_4": "Vé máy bay & booking khách sạn.",
                "cta_subtitle": "Tra cứu chi tiết yêu cầu hồ sơ",
                "cta_button_text": "Tra cứu yêu cầu hồ sơ",
                "cta_button_link": "/visa/ho-so-yeu-cau/",
            },
            "hoa-ky": {
                "hero_title": "Visa Mỹ – Hướng dẫn & lưu ý quan trọng",
                "hero_subtitle": "Giải thích DS-160, phỏng vấn và yêu cầu hồ sơ khi xin visa Mỹ.",
                "overview_title": "Tổng quan Visa Mỹ",
                "overview_content": (
                    "Visa Mỹ yêu cầu khai đơn DS-160 chính xác, phỏng vấn rõ ràng, hồ sơ tài chính và ràng buộc mạnh mẽ."
                ),
                "visa_types_summary": "Du lịch B1/B2, công tác, thăm thân",
                "visa_processing_time": "7–21 ngày (tùy lịch phỏng vấn)",
                "visa_highlight_note_1": "Khai DS-160 cần chính xác tuyệt đối.",
                "visa_highlight_note_2": "Phỏng vấn ngắn – cần trả lời đúng trọng tâm.",
                "visa_highlight_note_3": "Tài chính và ràng buộc ảnh hưởng mạnh đến kết quả.",
                "cta_title": "Giấy tờ cần chuẩn bị",
                "cta_featured_requirement_1": "Hộ chiếu & DS-160.",
                "cta_featured_requirement_2": "Giấy hẹn phỏng vấn.",
                "cta_featured_requirement_3": "Tài chính và lịch sử du lịch.",
                "cta_featured_requirement_4": "Giấy tờ công việc.",
                "cta_subtitle": "Tra cứu chi tiết yêu cầu hồ sơ",
                "cta_button_text": "Tra cứu yêu cầu hồ sơ",
                "cta_button_link": "/visa/ho-so-yeu-cau/",
            },
            "khoi-schengen": {
                "hero_title": "Visa Schengen – Đi châu Âu dễ dàng",
                "hero_subtitle": "Một visa – đi được 27 quốc gia. Cập nhật quy định Schengen 2025.",
                "overview_title": "Tổng quan Visa Schengen",
                "overview_content": (
                    "Visa Schengen yêu cầu lịch trình chi tiết, tài chính mạnh và bảo hiểm du lịch 30.000 EUR bắt buộc."
                ),
                "visa_types_summary": "Du lịch, thăm thân, công tác",
                "visa_processing_time": "10–21 ngày làm việc",
                "visa_highlight_note_1": "Bảo hiểm du lịch tối thiểu 30.000 EUR.",
                "visa_highlight_note_2": "Lịch trình chi tiết theo ngày.",
                "visa_highlight_note_3": "Chứng minh tài chính đầy đủ.",
                "cta_title": "Hồ sơ xin visa Schengen",
                "cta_featured_requirement_1": "Hộ chiếu hợp lệ.",
                "cta_featured_requirement_2": "Booking khách sạn & vé máy bay.",
                "cta_featured_requirement_3": "Sao kê ngân hàng 3–6 tháng.",
                "cta_featured_requirement_4": "Bảo hiểm du lịch chuẩn Schengen.",
                "cta_subtitle": "Tra cứu chi tiết yêu cầu hồ sơ",
                "cta_button_text": "Tra cứu yêu cầu hồ sơ",
                "cta_button_link": "/visa/ho-so-yeu-cau/",
            },
        }

        for slug, d in detail_data.items():
            country = countries.get(slug)
            if not country:
                continue
            detail, _ = CountryDetail.objects.get_or_create(country=country)
            for field, value in d.items():
                setattr(detail, field, value)
            detail.save()

        # COUNTRY SECTIONS
        section_base = {
            "uc": [
                {"title": "Hồ sơ đầy đủ, chính xác và trung thực", "content": (
                    "Điền thông tin trùng khớp với giấy tờ gốc như: hộ chiếu, giấy tờ tài chính, thư mời hoặc thư nhập học.\n\n"
                    "Không khai gian dối: Úc kiểm tra rất kỹ hồ sơ. Nếu bị phát hiện khai sai, visa có thể bị từ chối ngay lập tức.\n\n"
                    "Nhiều hồ sơ bị trì hoãn hoặc từ chối chỉ vì thiếu giấy tờ quan trọng (ví dụ: chứng minh tài chính, chứng minh mối quan hệ)."
                ), "image": "visa/country/sections/australia_financial.jpg"},
                {"title": "Biometrics", "content": "Bắt buộc cung cấp dữ liệu sinh trắc học sau khi nộp đơn.", "image": "visa/country/sections/australia_biometrics.jpg"},
                {"title": "Bảo hiểm du lịch", "content": "Khuyến nghị mua bảo hiểm du lịch suốt thời gian lưu trú.", "image": "visa/country/sections/australia_insurance.jpg"},
            ],
            "canada": [
                {"title": "Chứng minh tài chính", "content": "Sao kê ngân hàng, bảng lương và tài sản nếu có.", "image": "visa/country/sections/canada_financial.jpg"},
                {"title": "Lịch trình du lịch", "content": "Chuẩn bị lịch trình rõ ràng từng ngày.", "image": "visa/country/sections/canada_itinerary.jpg"},
                {"title": "Ràng buộc tại Việt Nam", "content": "Cần giấy tờ công việc hoặc tài sản.", "image": "visa/country/sections/canada_ties.jpg"},
            ],
            "hoa-ky": [
                {"title": "Khai DS-160", "content": "Mọi thông tin phải chính xác và trùng khớp.", "image": "visa/country/sections/usa_ds160.jpg"},
                {"title": "Phỏng vấn visa Mỹ", "content": "Trả lời ngắn gọn, trung thực và đúng trọng tâm.", "image": "visa/country/sections/usa_interview.jpg"},
                {"title": "Hồ sơ hỗ trợ", "content": "Tài chính, công việc, lịch sử du lịch giúp tăng tỉ lệ đậu.", "image": "visa/country/sections/usa_documents.jpg"},
            ],
            "khoi-schengen": [
                {"title": "Bảo hiểm du lịch", "content": "Mức tối thiểu 30.000 EUR là bắt buộc.", "image": "visa/country/sections/schengen_insurance.jpg"},
                {"title": "Lịch trình chuyến đi", "content": "Cần liệt kê chi tiết từng ngày.", "image": "visa/country/sections/schengen_itinerary.jpg"},
                {"title": "Chứng minh tài chính", "content": "Sao kê ngân hàng và chứng minh thu nhập.", "image": "visa/country/sections/schengen_financial.jpg"},
            ],
        }

        for slug, sections in section_base.items():
            country = countries.get(slug)
            if not country:
                continue
            for i, section in enumerate(sections):
                CountrySection.objects.update_or_create(
                    country=country,
                    title=section["title"],      # ❗ KHÔNG dùng order để lookup
                    defaults={
                        "content": section["content"],
                        "image": section["image"],
                        "image_left": (i % 2 == 0),
                        "order": i                # order chỉ nằm trong defaults
                    }
                )


        # TIPS
        tips_data = {
            "uc": [("tip", "Nên có lịch trình rõ ràng."), ("risk", "Tài chính không đủ mạnh.")],
            "canada": [("tip", "Hồ sơ công việc rõ ràng giúp tăng tỷ lệ đậu."), ("risk", "Lịch trình không chặt chẽ.")],
            "hoa-ky": [("tip", "Trả lời phỏng vấn ngắn gọn."), ("risk", "Khai DS-160 sai thông tin.")],
            "khoi-schengen": [("tip", "Chuẩn bị bảo hiểm đúng chuẩn."), ("risk", "Không chứng minh được tài chính.")],
        }

        for slug, items in tips_data.items():
            country = countries.get(slug)
            if not country:
                continue
            for i, (tip_type, text) in enumerate(items):
                CountryTip.objects.update_or_create(
                    country=country,
                    tip_type=tip_type,  # ❗ dùng field khác để lookup
                    defaults={
                        "content": text,
                        "order": i
                    }
                )

        # FAQ
        faq_category, _ = FAQCategory.objects.get_or_create(name="Visa – Câu hỏi chung")
        faq_items = [
            {"question": "Thời gian xét duyệt visa mất bao lâu?", "answer": "Tùy nước và loại visa, thường 7–30 ngày.", "countries": ["uc", "canada", "hoa-ky", "khoi-schengen"]},
            {"question": "Có cần chứng minh tài chính không?", "answer": "Hầu hết các nước yêu cầu chứng minh tài chính.", "countries": ["uc", "canada", "khoi-schengen"]},
            {"question": "Visa Mỹ có cần phỏng vấn không?", "answer": "Visa Mỹ bắt buộc phỏng vấn.", "countries": ["hoa-ky"]},
        ]

        for item in faq_items:
            faq, _ = FAQItem.objects.get_or_create(
                question=item["question"],
                defaults={"answer": item["answer"], "category": faq_category}
            )
            faq.countries.clear()
            for slug in item["countries"]:
                country = countries.get(slug)
                if country:
                    faq.countries.add(country)

        self.stdout.write(self.style.SUCCESS("🎉 DONE – Seed hoàn tất!"))

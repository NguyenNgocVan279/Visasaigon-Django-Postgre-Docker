from django.core.management.base import BaseCommand
from apps.company.models import CompanyProfile

class Command(BaseCommand):
    help = "Seed default company profile data"

    def handle(self, *args, **kwargs):
        if CompanyProfile.objects.exists():
            self.stdout.write(self.style.WARNING("⚠️ Company profile already exists. Skipped."))
            return

        CompanyProfile.objects.create(
            name="CÔNG TY TNHH VISA SÀI GÒN",
            domain="https://visasaigon.net",
            logo="company/logo.png",  # nhớ upload file thật nếu cần
            hotline="0938635925",
            email="hotro@visasaigon.net",
            address="Số 1B, Đường 30, P. An Khánh, TP.HCM",
            google_map="""
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3919.2650176926486!2d106.725050176356!3d10.791002931512542!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752606cfb56953%3A0x6d91b56ef69fa190!2zMWIgxJDGsOG7nW5nIFPhu5EgMzAsIFBoxrDhu51uZyBBbiBLaMOhbmgsIFRo4bunIMSQ4bupYywgVGjDoG5oIHBo4buRIEjhu5MgQ2jDrSBNaW5oIDcwMDAwMCwgVmlldG5hbQ!5e0!3m2!1sen!2s!4v1763957991922!5m2!1sen!2s"
                    width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"
                    referrerpolicy="no-referrer-when-downgrade"></iframe>
            """,
            facebook="https://www.facebook.com/visasaigon.net",
            tiktok="https://tiktok.com/@abc",
            youtube="https://youtube.com/visasaigon.net",
            zalo="https://zalo.me/0938635925",

            description="Công ty chuyên dịch vụ visa & du lịch.",
            normal_working_time="08:00 - 17:00",
            saturday_working_time="08:00 - 12:00",

            web_dev_partner="Pytech.asia",
            partner_web_link="https://pytech.asia",
        )

        self.stdout.write(self.style.SUCCESS("✅ Seeded company profile successfully!"))

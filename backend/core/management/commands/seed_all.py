import os
import pkgutil
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.apps import apps

class Command(BaseCommand):
    help = "Chạy tất cả các lệnh seed_* với thứ tự ưu tiên."

    # =============================
    # 1️⃣ DANH SÁCH ƯU TIÊN
    # =============================
    PRIORITY_SEEDS = [
        #🎉 File seed company infomation 
        "seed_company",

        #🎪 File seed country and document requirements
        "seed_visa_du_lich_uc",
        "seed_visa_tham_than_uc",
        "seed_visa_cong_tac_uc",
        "seed_visa_du_lich_canada",
        "seed_visa_tham_than_canada",
        "seed_visa_cong_tac_canada",
        "seed_visa_du_lich_usa",
        "seed_visa_tham_than_usa",
        "seed_visa_cong_tac_usa",
        "seed_visa_du_lich_schengen",
        "seed_visa_tham_than_schengen",
        "seed_visa_cong_tac_schengen",

        #🧧 File seed for page "country_detail"
        "seed_country_detail",
    ]

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("🔍 Đang tìm tất cả file seed..."))

        seed_commands = []

        # Duyệt qua toàn bộ apps để tìm file seed
        for app_config in apps.get_app_configs():
            app_path = os.path.join(app_config.path, "management", "commands")

            if not os.path.isdir(app_path):
                continue

            for module in pkgutil.iter_modules([app_path]):
                module_name = module.name
                if module_name.startswith("seed_") and module_name != "seed_all": # ❗ Loại bỏ seed_all để tránh vòng lặp
                    seed_commands.append(module_name)

        # =============================
        # 2️⃣ TÁCH SEED THEO ƯU TIÊN
        # =============================
        priority = [s for s in self.PRIORITY_SEEDS if s in seed_commands]
        remaining = [s for s in seed_commands if s not in self.PRIORITY_SEEDS]

        # Ghép lại thành thứ tự cuối cùng
        ordered = priority + remaining

        if not ordered:
            self.stdout.write(self.style.WARNING("⚠️ Không tìm thấy file seed nào!"))
            return

        self.stdout.write(self.style.SUCCESS("📌 Thứ tự seed sẽ chạy:"))
        for cmd in ordered:
            self.stdout.write(f"  → {cmd}")

        # =============================
        # 3️⃣ CHẠY TỪNG SEED THEO THỨ TỰ
        # =============================
        for cmd in ordered:
            self.stdout.write(self.style.NOTICE(f"🚀 Đang chạy: {cmd} ..."))
            call_command(cmd)

        self.stdout.write(self.style.SUCCESS("🎉 Chạy seed hoàn tất!"))

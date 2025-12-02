👜 Tất cả lệnh đều chạy trong terminal của root dự án - D:\projects\django\visasaigon-django-postgre-docker

# Kiểm tra thông tin trong container database (visasaigon_db):
docker exec visasaigon_db sh -c 'echo $POSTGRES_DB'
docker exec visasaigon_db sh -c 'echo $POSTGRES_USER'
docker exec visasaigon_db sh -c 'echo $POSTGRES_PASSWORD'
docker exec visasaigon_db sh -c 'echo $POSTGRES_HOST'
docker exec visasaigon_db sh -c 'echo $POSTGRES_PORT'
docker exec visasaigon_db sh -c 'echo $POSTGRES_PORT'

# Kiểm tra database nào tồn tại trong container "visasaigon_db":
docker exec -it visasaigon_db psql -U visasaigon -l

# Kiểm tra container "visasaigon_web" đang kết nối đến database theo thông tin nào:
docker exec -it visasaigon_web python manage.py shell -c "from django.conf import settings; print(settings.DATABASES)"

# Tạo app mới:
docker compose exec web mkdir apps/company      # "web" là tên service trong container
docker compose exec web python manage.py startapp company apps/company

# Xoá tất cả cả các file migrations (trừ trong app "accounts"):
Get-ChildItem -Path .\backend\apps -Recurse -Filter "*.py" |
    Where-Object { $_.DirectoryName -match "migrations" `
        -and $_.Name -ne "__init__.py" `
        -and $_.FullName -notmatch "backend\\apps\\accounts" } |
    Remove-Item

Get-ChildItem -Path .\backend\apps -Recurse -Include "*.pyc" |
    Where-Object {
        $_.DirectoryName -match "migrations" -and
        $_.FullName -notmatch "backend\\apps\\accounts"
    } |
    Remove-Item

# Xoá bảng trong database (trong PgAdmin4):
DROP TABLE IF EXISTS blog_blogcategory, blog_blogpost, blog_blogpost_tags, blog_blogtag, clients_application, clients_applicationfile, clients_client, faq_faqcategory, faq_faqitem, pages_page, visa_country, visa_requireddocument, visa_visatype, company_companyprofile, visa_countrydetail, visa_countrysection, visa_countrytip CASCADE;

# Xoá Volume trong docker (sẽ mất supperuser):
Bước 1: Dừng container: docker compose down
Bước 2: Xoá volume: docker volume rm visasaigon-django-postgre-docker_visasaigon_postgres_data
Bước 3: Khởi động lại container: docker compose up -d --build

#🎉 Tạo superuser:
docker compose exec web python manage.py createsuperuser

# Restart tất cả các container đang chạy:
docker restart $(docker ps -q)

#🎊 Seed data cho app "visa":
docker-compose exec web python manage.py seed_visa_data
docker-compose exec web python manage.py seed_all

# Tạo migrations & migrate
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate

# Mã màu:
Bộ 1: Sang – Dịu – Nữ tính (Tương sinh mạnh)

• Màu chính (primary):
#E02454
🔸 #FF6B6B – Đỏ coral mềm, hợp mệnh Hỏa, tạo cảm giác ấm và nữ tính.

• Màu phụ (secondary):
#003A66
🌿 #4CAF50 – Xanh lá (Mộc sinh Hỏa), mang lại may mắn & cân bằng.

• Màu nhấn (accent):
#6c757d
✨ #FFE66D – Vàng nhạt giúp tươi sáng, tạo điểm nhấn nhẹ nhàng.
#ffc107

#7B2D26

rgba(189, 76, 73, 1)

Màu lá chuối non chuẩn

👉 #A3D65C

🌿 Các biến thể đẹp khác

#9ED454 – lá chuối non sáng

#8BCB3F – lá chuối non hơi ngả xanh

#B4E77A – lá chuối non nhạt, mềm dịu

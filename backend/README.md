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

# Tạo superuser:
docker compose exec web python manage.py createsuperuser

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
DROP TABLE IF EXISTS clients_applicationfile CASCADE;e
...

# Xoá Volume trong docker:
Bước 1: Dừng container: docker compose down
Bước 2: Xoá volume: docker volume rm visasaigon-django-postgre-docker_visasaigon_postgres_data
Bước 3: Khởi động lại container: docker compose up --build


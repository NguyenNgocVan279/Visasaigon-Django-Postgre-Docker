# apps/visa/utils.py
import os
from datetime import datetime

def application_file_upload_path(instance, filename):
    """
    Tạo đường dẫn upload:
    clients/<client_name>/<YYYY>/<MM>/<DD>/<file>

    File name format:
    file_type_clientName_YYYYMMDD.ext
    hoặc thêm _2, _3 nếu trùng
    """

    # Lấy tên client
    client_name = f"{instance.application.client.last_name}_{instance.application.client.first_name}"
    client_name = client_name.replace(" ", "_")

    # Loại file: passport, id_card, invitation...
    file_type = instance.file_type

    # Ngày
    today = datetime.now()
    date_folder = today.strftime("%Y/%m/%d/")
    date_str = today.strftime("%Y%m%d")

    # Lấy extension
    ext = filename.split('.')[-1]

    # Tên file gốc
    base_filename = f"{file_type}_{client_name}_{date_str}"
    new_filename = f"{base_filename}.{ext}"

    # Thư mục
    folder = f"clients/uploads/{client_name}/{date_folder}"

    # Path tuyệt đối tới thư mục trên server
    full_folder_path = os.path.join("media", folder)

    # Tạo thư mục nếu chưa có
    os.makedirs(full_folder_path, exist_ok=True)

    # Nếu file trùng —> tăng số thứ tự
    final_filename = new_filename
    counter = 1

    while os.path.exists(os.path.join(full_folder_path, final_filename)):
        counter += 1
        final_filename = f"{base_filename}_{counter}.{ext}"

    return folder + final_filename

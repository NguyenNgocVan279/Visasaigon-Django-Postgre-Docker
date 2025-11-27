✨ CÁC PHẦN CHÍNH: (qv1Er2FS)
1️⃣ Chuẩn bị VPS (1-time)
2️⃣ Chuẩn bị repository & secrets trên GitHub
3️⃣ Tạo workflow CI/CD (GitHub Actions) để deploy tự động

✨ CHI TIẾT THỰC HIỆN CÁC PHẦN:
🎉 Phần A — Chuẩn bị VPS trên IONOS (làm 1 lần):
Mục tiêu: tạo user không phải root, cấu hình SSH key, cài Docker + Docker Compose plugin, tạo thư mục dự án, cấu hình firewall.
1. Tạo VPS & SSH key:
    - Tạo VPS (Ubuntu 22.04 recommended) trong IONOS cloud panel.
    - Tạo cặp SSH key trên máy local (nếu chưa có): (lệnh kiểm tra: ls ~/.ssh, lệnh xoá cặp key: rm ~/.ssh/id_ed25519, rm ~/.ssh/id_ed25519.pub)
            # local machine
            ssh-keygen -t ed25519 -C "nguyenngocvan279@gmail.com" -f C:\Users\ThinkPad\.ssh\ionos_deploy
    - Upload public key (~/.ssh/ionos_deploy.pub) vào IONOS VM hoặc panel theo hướng dẫn IONOS (SSH Keys). Kể cả dùng password lần đầu, bạn nên dùng SSH key:
            ✅ Cách mở file "ionos_deploy.pub": cat ~/.ssh/ionos_deploy.pub
            ✅ CÁCH ADD SSH KEY LÊN VPS IONOS (IONOS VPS (gói rẻ) không có mục SSH Keys trên giao diện web):
                Bước 1 — Login vào VPS bằng password: ssh root@217.154.167.123 → nhập password IONOS gửi qua email.
                Bước 2 — Tạo thư mục .ssh trên VPS: mkdir -p ~/.ssh
                Bước 3 — Thêm public key vào file authorized_keys:
                    Trên máy bạn (Windows), chạy: cat ~/.ssh/ionos_deploy.pub → Copy toàn bộ dòng public key.
                    Quay lại terminal VPS và chạy: echo "=== PASTE PUBLIC KEY TẠI ĐÂY ===" >> ~/.ssh/authorized_keys
                        echo "ssh-ed25519 AAAAC3NzaC1lZDI1N...." >> ~/.ssh/authorized_keys
                Bước 4 — Set đúng permission:
                    chmod 700 ~/.ssh
                    chmod 600 ~/.ssh/authorized_keys
                Bước 5 — Thoát VPS: exit

    - Kết nối thử: "ssh -i ~/.ssh/ionos_deploy root@217.154.167.123"

2. Tạo user deploy (không dùng root):
    - Lý do:
        👉 rất quan trọng vì:
            root login trực tiếp = nguy hiểm
            Nhiều dịch vụ yêu cầu user thường
    - Tạo user: "adduser deploy":
        Nhập password (có thể đặt tạm)
        Các câu hỏi khác → nhấn ENTER bỏ qua
    - Cho user mới quyền sudo: "usermod -aG sudo deploy"
    - Copy SSH key sang user mới "deploy": 
        sudo mkdir -p /home/deploy/.ssh
        🎉sudo cp /root/.ssh/authorized_keys /home/deploy/.ssh/
        sudo chown -R deploy:deploy /home/deploy/.ssh
        sudo chmod 700 /home/deploy/.ssh
        sudo chmod 600 /home/deploy/.ssh/authorized_keys
        
    - Cấu hình SSH bảo mật:
        👉Trên VPS (với user deploy hoặc root): Mở file SSH config:
            sudo nano /etc/ssh/sshd_config
        👉Tìm các dòng sau (dùng Ctrl+W để tìm) và sửa thành:
            PasswordAuthentication no (Nếu dòng có # thì xoá #)
        👉Lưu file: Ctrl+O, Enter, Ctrl+X
        👉Reload SSH: sudo systemctl restart ssh

    - Bây giờ bạn có thể SSH bằng deploy user không dùng root trực tiếp:
        ssh -i ~/.ssh/ionos_deploy deploy@217.154.167.123 → kết quả: deploy@romantic-stonebraker:~$
    - Khi cần thao tác root, dùng: sudo command

3. Cài Docker & Docker Compose (plugin) trên VPS:
# đăng nhập bằng user deploy (hoặc sudo)
✅ Cách bật sudo không password (AN TOÀN & CHUẨN):
    Chạy lệnh này bằng root: "sudo visudo"
    Trong file mở ra, thêm dòng sau bên dưới: deploy ALL=(ALL) NOPASSWD:ALL
    Ví dụ cuối file:
        # User privilege specification
        root    ALL=(ALL:ALL) ALL
        deploy  ALL=(ALL) NOPASSWD:ALL
    Save lại.
    ✅ Kiểm tra
        Đăng nhập bằng deploy: ssh deploy@YOUR_SERVER_IP
        Sau đó: "sudo ls" → Nếu không hỏi password ✅ thành công
    ✅ Sau khi bật NOPASSWD:
        CI/CD mới chạy được: "sudo docker-compose -f docker-compose.prod.yml up -d --build"

✅ Chạy lệnh: sudo apt update && sudo apt upgrade -y
# cài các package cần thiết
sudo apt install -y ca-certificates curl gnupg lsb-release
# add docker gpg key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
# kiểm tra
sudo docker run hello-world

# Thêm user deploy vào group docker để chạy docker không cần sudo:
sudo usermod -aG docker deploy

# đăng xuất và đăng nhập lại để group mới có hiệu lực

4. Tạo thư mục dự án & quyền:
# ví dụ đặt project ở /srv/visasaigon-django-postgre-docker:
sudo mkdir -p /srv/visasaigon-django-postgre-docker
sudo chown -R deploy:deploy /srv/visasaigon-django-postgre-docker

5. (Tùy chọn) Cài certbot (Let's Encrypt) / Nginx sau khi deploy:
Bạn có thể dùng Nginx trong container (cách mình hướng dẫn) và dùng certbot trên host hoặc container để cấp SSL. IONOS có docs Let's Encrypt.

🎉 Phần B — Chuẩn bị repo GitHub & secrets:
Bạn có cấu trúc visasaigon-django-postgre-docker/ như mô tả. Ta cần:
    Thêm file docker-compose.prod.yml (nếu chưa có) và cấu hình env_file: - .env.prod trong service web.
    Tạo .env.example (commit), không commit .env hay .env.prod.
    Trên GitHub repo: vào Settings → Secrets and variables → Actions thêm secrets sau:
    🎊BẮT BUỘC
        DEPLOY_HOST — IP hoặc hostname VPS
        DEPLOY_USER — deploy
        DEPLOY_SSH_KEY — private key (nội dung của ~/.ssh/ionos_deploy, copy paste - là file private key trên laptop)
        DEPLOY_PORT — (mặc định 22) nếu khác
        ENV_PROD — (tùy chọn) nội dung file .env.prod (nếu bạn muốn workflow tạo file env trên server). Lưu ý: để an toàn, bạn có thể lưu các biến riêng lẻ thay vì 1 blob.
    🎊TÙY CHỌN (nếu dùng Docker registry)
        REGISTRY_USER, REGISTRY_PASSWORD, REGISTRY_URL — nếu bạn build & push image tới registry riêng.

🎉 Phần C — Chiến lược deploy CI/CD:
Có 2 cách chính:
A. Build & deploy trên VPS bằng Git pull (ít phức tạp): workflow SSH tới server → git -C /srv/backend pull → docker compose -f docker-compose.prod.yml pull → docker compose -f docker-compose.prod.yml up -d --build --remove-orphans.
B. Build image trong Actions, push vào registry → trên server docker compose pull → up. (ít network và nhanh hơn khi nhiều server)
Mình sẽ cung cấp mẫu workflow cho phương án A (nhiều bạn dùng) vì đơn giản, không cần registry.





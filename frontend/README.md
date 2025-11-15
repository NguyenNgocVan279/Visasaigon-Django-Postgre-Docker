# Build image
docker compose build

# Vừa build image, vừa tạo containers
docker compose up

# Luôn buil lại, vừa tạo image, vừa tạo container
docker compose up --build

# Tạo containers (khi đã có sẵn image)
docker compose up -d

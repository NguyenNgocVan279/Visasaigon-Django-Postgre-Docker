# ==============================
# Dockerfile cho Django app
# ==============================
# Base image: Python 3.13.9 slim
FROM python:3.13.9-slim

# ==============================
# Thiết lập biến môi trường
# ==============================
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/usr/local/bin:$PATH"

# ==============================
# Tạo thư mục làm việc
# ==============================
WORKDIR /app

# ==============================
# Cài các package hệ thống cần build
# ==============================
RUN apt-get update && \
    apt-get install -y build-essential libpq-dev gcc && \
    apt-get install -y netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

# ==============================
# Copy và cài requirements
# ==============================
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ==============================
# Copy toàn bộ code vào container
# ==============================
COPY . /app/

# ==============================
# Copy entrypoint và cho phép chạy
# ==============================
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# ==============================
# Expose port 8000 (container)
# ==============================
EXPOSE 8000

# ==============================
# Entrypoint
# ==============================
ENTRYPOINT ["/entrypoint.sh"]

# Entry point
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]

import multiprocessing

# Server socket
bind = "0.0.0.0:8000"   # Django chạy tại port 8000 trong container

# Worker settings
workers = multiprocessing.cpu_count() * 2 + 1   # auto scale theo CPU
worker_class = "uvicorn.workers.UvicornWorker"  # tối ưu ASGI (Django 4+ chạy tốt)
threads = 2
max_requests = 1000
max_requests_jitter = 100

# Timeouts
timeout = 120
keepalive = 5
graceful_timeout = 30

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Django recommended
capture_output = True
enable_stdio_inheritance = True

# Performance tuning
preload_app = True

# Limit request size (optional)
limit_request_field_size = 8190
limit_request_line = 4094

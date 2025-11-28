import multiprocessing

# ================================
# Bind
# ================================
bind = "0.0.0.0:8000"

# ================================
# Workers — Stable for Django
# ================================
workers = 3               # ổn định cho CPU 1–2 core
worker_class = "sync"     # Django WSGI chuẩn nhất

# ================================
# Worker threads (chỉ dùng khi gthread)
# threads = 2

# ================================
# Auto-restart to avoid memory leak
# ================================
max_requests = 1000
max_requests_jitter = 100

# ================================
# Timeouts
# ================================
timeout = 60
graceful_timeout = 30
keepalive = 5

# ================================
# Logging
# ================================
accesslog = "-"
errorlog = "-"
loglevel = "info"

# ================================
# Django recommended
# ================================
capture_output = True
enable_stdio_inheritance = True

# ================================
# Performance
# ================================
preload_app = True

# ================================
# Security limits
# ================================
limit_request_field_size = 8190
limit_request_line = 4094

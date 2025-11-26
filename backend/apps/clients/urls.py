from django.urls import path
from . import views

app_name = "clients"

urlpatterns = [
    path("dang-ky-lam-visa/", views.submit_application, name="dang-ky-lam-visa"),
    path("dang-ky-thanh-cong/", views.success, name="dang-ky-thanh-cong"),
]

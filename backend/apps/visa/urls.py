from django.urls import path
from . import views

app_name = "visa"

urlpatterns = [
    path("ho-so-yeu-cau/", views.document_requirements, name="ho-so-yeu-cau"),
    path("visa-cac-nuoc/", views.country_list, name="visa-cac-nuoc"),
    path('<slug:country_slug>/', views.country_detail, name='country_detail'),
]

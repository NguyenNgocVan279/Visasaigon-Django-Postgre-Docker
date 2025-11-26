from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path('', views.home, name='trang-chu'),
    path('gioi-thieu/', views.about, name='gioi-thieu'),
    path('lien-he/', views.contact, name='lien-he'),
    
    path('dich-vu-visa-uc/', views.about, name='dich-vu-visa-uc'),
    path('dich-vu-visa-canada/', views.about, name='dich-vu-visa-canada'),
    path('dich-vu-visa-usa/', views.about, name='dich-vu-visa-usa'),
    path('dich-vu-visa-chau-au/', views.about, name='dich-vu-visa-chau-au'),

    path("lien-he/submit/", views.contact_submit, name="contact_submit"),  # Ajax submit
]

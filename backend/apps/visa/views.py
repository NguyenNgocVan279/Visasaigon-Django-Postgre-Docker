from django.shortcuts import render, get_object_or_404
from .models import Country, VisaType, RequiredDocument, CountryDetail, CountrySection, CountryTip
from apps.faq.models import FAQItem

def document_requirements(request):
    countries = Country.objects.all().order_by("name")
    visa_types = None
    documents = None

    selected_country = request.GET.get("country")
    selected_visa_type = request.GET.get("visa_type")

    # Nếu chọn country → load visa type
    if selected_country:
        visa_types = VisaType.objects.filter(country_id=selected_country)

    # Nếu chọn đủ 3 mục → load documents
    if selected_country and selected_visa_type:
        documents = RequiredDocument.objects.filter(
            country_id=selected_country,
            visa_type_id=selected_visa_type,
        )

    context = {
        "countries": countries,
        "visa_types": visa_types,
        "documents": documents,
        "selected_country": selected_country,
        "selected_visa_type": selected_visa_type,
    }
    return render(request, "visa/requirements.html", context)

def country_list(request):
    countries = Country.objects.all()
    return render(request, "visa/country_list.html", {"countries": countries})

# -----------------------------
# Trang chi tiết quốc gia
# -----------------------------
def country_detail(request, country_slug):
    country = get_object_or_404(Country, slug=country_slug)
    
    # Chi tiết tổng quan
    detail = getattr(country, "detail", None)
    
    # Các loại visa
    visa_types = country.visa_types.all()
    
    # Sections xen kẽ ảnh - text
    sections = country.sections.all()
    
    # Tips / Risk
    tips = country.tips.all()
    
    # FAQ liên quan country
    faqs = FAQItem.objects.filter(countries=country).select_related('category').order_by('order')
    
    context = {
        "country": country,
        "detail": detail,
        "visa_types": visa_types,
        "sections": sections,
        "tips": tips,
        "faqs": faqs,
    }
    return render(request, "visa/country_detail.html", context)

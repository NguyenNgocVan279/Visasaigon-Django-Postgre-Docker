from .models import CompanyProfile

def company_profile(request):
    profile = CompanyProfile.objects.first()
    return {"profile": profile}

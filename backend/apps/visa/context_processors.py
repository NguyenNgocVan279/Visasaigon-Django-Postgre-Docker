from .models import Country

def visa_countries(request):
    return {
        "visa_countries": Country.objects.all()
    }

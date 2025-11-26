from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, "pages/home.html")

def about(request):
    return render(request, "pages/about.html")

def contact(request):
    return render(request, "pages/contact.html")

@csrf_exempt  # Nếu dùng AJAX từ JS, CSRF token đã gửi thì có thể bỏ, hoặc giữ fetch header
def contact_submit(request):
    """Xử lý AJAX POST gửi thông tin contact"""
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        main_need = request.POST.get("main_need")
        detail_need = request.POST.get("detail_need")

        # Lưu vào model nếu muốn
        # contact = Contact.objects.create(name=name, phone=phone, main_need=main_need, detail_need=detail_need)

        return JsonResponse({"message": "Gửi yêu cầu thành công!"})

    return JsonResponse({"message": "Phương thức không hợp lệ."}, status=400)

from django.shortcuts import render, redirect
from django.forms import modelformset_factory

from .forms import ClientForm, ApplicationForm, ApplicationFileFormSet
from .models import Client, Application, ApplicationFile


def submit_application(request):
    if request.method == "POST":
        client_form = ClientForm(request.POST)
        app_form = ApplicationForm(request.POST)
        file_formset = ApplicationFileFormSet(
            request.POST,
            request.FILES,
            queryset=ApplicationFile.objects.none(),
        )

        if client_form.is_valid() and app_form.is_valid() and file_formset.is_valid():

            # 1. Tạo Client
            client = client_form.save()

            # 2. Tạo Application
            application = app_form.save(commit=False)
            application.client = client
            application.save()

            # 3. Lưu Application Files
            for form in file_formset:
                if form.cleaned_data and form.cleaned_data.get("file"):
                    file_obj = form.save(commit=False)
                    file_obj.application = application
                    file_obj.save()

            return redirect("clients:dang-ky-thanh-cong")

    else:
        client_form = ClientForm()
        app_form = ApplicationForm()
        file_formset = ApplicationFileFormSet(queryset=ApplicationFile.objects.none())

    return render(request, "clients/application_form.html", {
        "client_form": client_form,
        "app_form": app_form,
        "file_formset": file_formset,
    })


def success(request):
    return render(request, "clients/success.html")

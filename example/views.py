from django.shortcuts import render
from django.http import HttpResponse

from .forms import CapturePhoneNumbers

def index(request):
  form = CapturePhoneNumbers()
  numbers = "Enter phone numbers and they will appear below"
  if request.method == "POST":
    numbers = request.POST.get("prospective_customers")
  return render(request, "example/index.html", {"form": form, "phone_numbers": numbers})

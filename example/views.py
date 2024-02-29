from django.shortcuts import render
from django.http import HttpResponse

from .forms import CapturePhoneNumbers

def index(request):
  form = CapturePhoneNumbers()
  return render(request, "example/index.html", {"form": form})

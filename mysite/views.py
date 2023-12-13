from django.shortcuts import render
from django.http import HttpResponse, FileResponse, JsonResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def video_list(request):
    return render(request, "video_list.html")

def company_list(request):
    return render(request, "company_list.html")

def product_list(request):
    return render(request, "product_list.html")
from django.shortcuts import render
from django.http import HttpResponse, FileResponse, JsonResponse
from mysite import models

# Create your views here.

def index(request):
    return render(request, "index.html")

# def video(request):
#     return render(request, "videolist.html")

def company(request):
    brna=models.Company.objects.all()
    return render(request, "company.html",locals())

# def product(request):
#     return render(request, "productlist.html")
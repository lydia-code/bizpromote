from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse, JsonResponse
from mysite import models
from mysite.forms import brandForm

# Create your views here.

def index(request):
    categories = models.Category.objects.all()
    return render(request, "index.html",locals())

def category(request, id):
    target_category = models.Category.objects.get(id=id)
    brands = target_category.brand_set.all()
    return render(request, "category.html", locals())

# def video(request):
#     return render(request, "videolist.html")

def list(request):
    brands = models.Brand.objects.all()
    return render(request, "list.html", locals())

def brand(request, id):
    brand  = models.Brand.objects.get(id=id)
    return(request, 'brand.html', locals())

def test(request, id):
    return(request, 'test.html', locals())
# def product(request):
#     return render(request, "productlist.html")

def addbrand(request):
    if request.method == "POST":
        data = brandForm(request.POST, request.FILES)
        if data.is_valid():
            data.save()
        return redirect("/addbrand/")
    else:
        form = brandForm()
    brands = models.Brand.objects.all().order_by('-id')
    return render(request, "addbrand.html",locals())
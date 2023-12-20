from django.contrib import admin
from mysite import models
from mysite.models import Category, Brand
# from mysite.models import Person, Company, Video, Photo
# Register your models here.

# class PersonAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(models.Person, PersonAdmin)

# @admin.register(Person)
# class PersonAdemin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name']

# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):
#     pass
#     #list_display = ['name', 'introdcution','website', 'email','telephone']

# @admin.register(Video)
# class VideoAdmin(admin.ModelAdmin):
#     list_display = ['name','link']

# @admin.register(Photo)
# class PhotiAdmin(admin.ModelAdmin):
#     list_display = ['name','link']

@admin.register(Category)
class PersonAdemin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']



from django.contrib import admin
from mysite import models
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Person, PersonAdmin)
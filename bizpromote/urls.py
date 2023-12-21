"""
URL configuration for bizpromote project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from mysite import views
from django.urls import path, include

list_patterns =[
    path('',views.list, name='list'),
    # path('add', views.comapny_add),
    # path('delete/<int:id>', views.company_delete)

]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('list/', include(list_patterns)),
    path('category/<int:id>/', views.category),
    path('brand/<int:id>/', views.brand),
    path('test/<int:id>/', views.test),
    path('addbrand/', views.addbrand)
    #path('video/', views.video, name='video')
]

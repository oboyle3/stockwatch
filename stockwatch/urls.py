"""
URL configuration for stockwatch project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path

from core.views import addstock, delete_stock, homepage#added
from core.views import dashboard, mlb

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage, name='homepage'),
    path('dashboard/',dashboard, name='dashboard'),
    path('addstock/',addstock, name='addstock'),
    path("delete/<int:id>/", delete_stock, name="delete_stock"),
    path('mlb/', mlb ,name="mlb")
]

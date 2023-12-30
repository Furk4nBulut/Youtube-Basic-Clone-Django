"""
URL configuration for Youtube project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin

class NoPasswordAdminSite(admin.AdminSite):
    def has_permission(self, request):
        return request.user.is_active  # Sadece aktif kullanıcılara izin ver

# Yeni AdminSite'i kullanarak admin URL'lerini tanımla
admin.site = NoPasswordAdminSite()

# URL'leri tanımla
urlpatterns = [
    path('admin/', admin.site.urls),
    # diğer url'ler...
]

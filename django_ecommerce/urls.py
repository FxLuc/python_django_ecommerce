"""django_ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django_ecommerce import settings
from django_ecommerce import settings
from django_ecommerce_app import views
from django_ecommerce_app import adminviews
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', views.admin_login, name="admin_login"),
    path('index', views.index),

    # ADMIN
    path('admin_home', adminviews.admin_home, name="admin_home"),
    path('admin_login_process',views.admin_login_process,name="admin_login_process"),
    path('admin_logout_process',views.admin_logout_process,name="admin_logout_process"),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

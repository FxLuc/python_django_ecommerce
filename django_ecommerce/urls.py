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
from django_ecommerce_app import views
from django_ecommerce_app import adminviews
from django.conf.urls.static import static


urlpatterns = [
    path('index', views.index),

    # ADMIN
    path('admin/', views.admin_login, name="admin_login"),
    path('admin_login_process',views.admin_login_process,name="admin_login_process"),
    path('admin_logout_process',views.admin_logout_process,name="admin_logout_process"),
    path('admin_home', adminviews.admin_home, name="admin_home"),
    #CATEGORIES
    path('category_list',adminviews.CategoriesListView.as_view(),name="category_list"),
    path('category_create',adminviews.CategoriesCreate.as_view(),name="category_create"),
    path('category_update/<slug:pk>',adminviews.CategoriesUpdate.as_view(),name="category_update"),
    #SUBCATEGORIES
    path('sub_category_list',adminviews.SubCategoriesListView.as_view(),name="sub_category_list"),
    path('sub_category_create',adminviews.SubCategoriesCreate.as_view(),name="sub_category_create"),
    path('sub_category_update/<slug:pk>',adminviews.SubCategoriesUpdate.as_view(),name="sub_category_update"),
    #Merchant User
    path('merchant_create',adminviews.MerchantUserCreateView.as_view(),name="merchant_create"),
    path('merchant_list',adminviews.MerchantUserListView.as_view(),name="merchant_list"),
    path('merchant_update/<slug:pk>',adminviews.MerchantUserUpdateView.as_view(),name="merchant_update"),

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

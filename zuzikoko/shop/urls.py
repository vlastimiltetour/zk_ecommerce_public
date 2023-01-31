from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('products/', views.products, name='products'),
    path('about/', views.about, name='about'),
    path('<slug:category_slug>/', views.products, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('', views.home, name='home'),
]   
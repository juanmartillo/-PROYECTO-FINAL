from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('<slug:slug>', views.productDetail, name='productDetail'),
    path('search/<slug:category_slug>', views.category_list, name='category_list')
]

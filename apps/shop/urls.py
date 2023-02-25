from django.urls import path
from .views import ViewShop, ViewProduct


app_name = 'shop'

urlpatterns = [
    path('', ViewShop.as_view(), name='shop'),
    path('', ViewProduct.as_view(), name='product-single'),
 ]
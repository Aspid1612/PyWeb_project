from django.urls import path
from .views import ViewCart, ViewWishlist, ViewCartBuy, ViewCartDel, ViewCartAdd, ViewWishlistAdd, ViewWishlistDel


app_name = 'cart_shop'

urlpatterns = [
    path('', ViewCart.as_view(), name='cart'),
    path('wishlist/', ViewWishlist.as_view(), name='wishlist'),
    path('add/<int:product_id>', ViewCartAdd.as_view(), name='add_to_cart'),
    path('buy/<int:product_id>', ViewCartBuy.as_view(), name='buy'),
    path('del/<int:item_id>', ViewCartDel.as_view(), name='del_from_cart'),
    path('addwish/<int:product_id>', ViewWishlistAdd.as_view(), name='add_to_wishlist'),
    path('delwish/<int:item_id>', ViewWishlistDel.as_view(), name='del_to_wishlist'),

]
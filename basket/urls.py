from django.urls import path
from .views import basket_add, basket_remove, basket_detail, checkout, done
from .basket import Basket

urlpatterns = [
    path('', basket_detail, name='detail_basket'),
    path('add/<int:product_id>/', basket_add, name='add_basket'),
    path('remove/<int:product_id>/', basket_remove, name='remove_basket'),
    path('checkout/', checkout, name='checkout'),
    path('done/', done, name='done'),
]
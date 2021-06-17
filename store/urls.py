from django.urls import path
from . import views # importing the views from views.py


urlpatterns = [
    path('',views.store,name='store'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
]

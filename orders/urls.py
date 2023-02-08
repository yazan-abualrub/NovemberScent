from django.urls import path
from . import views

urlpatterns = [
    path('addToCart/', views.addToCart, name='addToCart'),
    path('cart/', views.cart, name='cart'),
    path('RemoveFromCart/<int:orderdetails_id>', views.RemoveFromCart, name='RemoveFromCart'),
    path('AddQty/<int:orderdetails_id>', views.AddQty, name='AddQty'),
    path('SubQty/<int:orderdetails_id>', views.SubQty, name='SubQty'),
    path('payment/', views.payment, name='payment'),
    path('myorders/', views.Myorders, name='myorders'),

]
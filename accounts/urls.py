from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('Edit/', views.Edit, name='Edit'),
    path('product_fav/<int:pro_id>', views.product_fav, name='product_fav'),
    path('showFav/', views.showFav, name='showFav'),


]

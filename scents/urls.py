from django.urls import path
from . import views

urlpatterns = [
    path('', views.scents, name='scents'),
    path('<int:pro_id>/', views.scent, name='scent'),
    path('ScentType/<int:category_id>', views.ScentType, name='ScentType'),

]
from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('gettypes/', views.gettypes, name='types'),
  path('productDetail/<int:id>', views.productDetail, name='details'),
  path('newProduct/', views.newProduct, name='newproduct'),
]

from django.urls import path
from shop import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories', views.categories, name='Categories'),
    path('product/<int:pid>', views.product, name='Product'),
    path('checkout', views.checkout, name='Checkout'),
    path('about', views.about, name='About'),
    path('cart', views.cart, name='Cart'),
    path('help', views.help, name='Help'),
    path('search', views.search, name='Search'),
    path('myorders', views.myorders, name='My_Orders')
]
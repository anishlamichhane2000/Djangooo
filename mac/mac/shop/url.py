from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name="ShopHome"),
path('about/', views.about,name="aboutus"),
path('contact/', views.contact,name="Contactus"),
path('traker/', views.tracker,name="Trakingstatus"),
path('search/', views.search,name="search"),
path('product/', views.product,name="productview"),
path('checkout/', views.checkout,name="checkout") ,
]
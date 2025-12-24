from django.urls import path
from  . import views

app_name = 'listings' # Django 4.2之後加app_name

#define the end point : index , about. Do it in views.py
urlpatterns = [
  path('',views.listings,name='index'),
  path('<int:listing_id>/',views.listing,name='listing'),# int 係datatype
  path('search/',views.search,name='search'),
]
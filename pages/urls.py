from django.urls import path
from  . import views

app_name = 'pages' # Django 4.2之後加app_name

#define the end point : index , about. Do it in views.py
urlpatterns = [
  path('',views.index,name = 'index'),
  path('about',views.about,name='about'),
  # path('listings',views.listing,name='listings'),
]
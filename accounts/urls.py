from django.urls import path
from  . import views

app_name = 'accounts' # Django 4.2之後加app_name
# step 1 , add path
#define the end point : index , about. Do it in views.py
urlpatterns = [
  path('signin/',views.login,name = 'login'),
  path('logout/',views.logout,name='logout'),
  path('register/',views.register,name='register'),
  path('dashboard/',views.dashboard,name='dashboard'),
]
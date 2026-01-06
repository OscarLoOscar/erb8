"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# define endpoint
# 多人用放上面
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls
# 2.Django 2次分流 -> RESTFul api -> /(Resources)/Endpoint -> 分endpoint
# empty string + empty string 既分流，但無得用empty string，所以起個folder： pages
urlpatterns = [
    path('',include('pages.urls',namespace='pages')),
    path('listings/', include('listings.urls',namespace='listings')),
    path('contacts/', include('contacts.urls',namespace='contacts')),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) + debug_toolbar_urls() # 要同一行，隔行會error
    
admin.site.site_header = 'Clinic Administration'
admin.site.site_title = 'Clinic Admin Portal'
admin.site.index_title = 'Welcome to Clinic Portal'
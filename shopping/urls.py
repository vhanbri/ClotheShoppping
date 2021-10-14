"""shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from onlineShopping import views

urlpatterns = [
   path('admin/', admin.site.urls),
   path('',views.MyIndexView.as_view(),name="index_view"), 
  
   
   path('login/',views.logInView.as_view(),name="login_view"),
   path('register/',views.RegisterView.as_view(),name="register_view"),
   path('products/',views.DashboardView.as_view(), name="product_view"),
    path('about/',views.AboutView.as_view(), name="about_view"),
    path('contact/',views.ContactView.as_view(), name="contact_view"),
   

]

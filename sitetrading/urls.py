"""sitetrading URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from sitetrading import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blogsingle/', views.blog_single, name='blogsingle'),
    path('blog/', views.blog, name ='blog'),
    path('contact/', views.contact, name='contact'),
    path('index/', views.index, name='index'),
    path('portfoliodetails/', views.portfolio_details, name='portfoliodetails'),
    path('portfolio/', views.portfolio,name ='portfolio'),
    path('pricing/', views.pricing, name='pricing'),
    path('services/', views.services, name='services'),
    path('testimonials/', views.testimonials, name='testimonials'),
]

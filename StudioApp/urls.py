from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('services/', views.services),
    path('booking/', views.booking),
    path('contact/', views.contact),
    path('shots/', views.shots),
    path('creative/', views.creative),
    path('wedding/', views.wedding),
    path('fashion/', views.fashion),
    path('portfolio/', views.portfolio),
    path('birthday/', views.birthday),
    path('agricultural/', views.agricultural),
    path('adventural/', views.adventural),
    path('festival/', views.festival),
    path('newborn/', views.newborn),
    path('reply/',views.reply),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

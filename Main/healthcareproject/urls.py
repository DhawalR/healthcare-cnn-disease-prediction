from django.contrib import admin
from django.urls import path
from healthapp.views import index, heartApp, diabetesApp, lungsApp, about

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index),
    path('heartApp/', heartApp, name='heartApp'),
    path('diabetesApp/', diabetesApp, name='diabetesApp'),
    path('lungsApp/', lungsApp, name='lungsApp'),
    path('about/', about, name='about'),
]

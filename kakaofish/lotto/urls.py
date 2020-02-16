from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_btn, name='start'),
    path('number/', views.get_number, name='getNum')
]

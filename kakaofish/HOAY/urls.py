from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hoaymain, name="hoyamain"),
    path('result/', views.result, name="hoyaresult"),
]
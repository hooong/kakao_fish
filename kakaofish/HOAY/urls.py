from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hoaymain, name="hoaymain"),
    path('result/<str:gender>/<str:age>/<str:realage>', views.result, name="hoayresult"),
    path('predict/<str:filename>', views.predictAge, name='predictAge'),
    path('error/', views.error, name='error')
]
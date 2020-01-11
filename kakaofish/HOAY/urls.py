from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hoaymain, name="hoaymain"),
    path('result/<int:id>', views.result, name="hoayresult"),
    path('predict/<int:id>', views.predictAge, name='predictAge'),
    path('error/', views.error, name='error')
]
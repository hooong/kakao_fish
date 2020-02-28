from django.contrib import admin
from django.urls import path
from . import views
from .scheduler import schedule

urlpatterns = [
    path('', views.coIndex, name="coIndex"),
    path('goodnews/',views.goodnews, name="goodnews")
]

# 크롤링 스케쥴러
schedule()
from django.contrib import admin
from django.urls import path
from myapi import views

urlpatterns = [
    path('', views.index, name="index"),
    path('get/', views.test_api, name="test_api"),
    path('get/<int:pk>', views.test_api_list, name="test_api_detail"),
    
]
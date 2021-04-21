from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.english,name='english'),
    path('thank',views.thank,name='thanks')

]
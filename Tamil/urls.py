from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.tamil,name='tamil'),
    path('thank',views.thank,name='thanks')

]
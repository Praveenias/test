from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.chemistry,name='chemistry'),
    path('thank',views.thank,name='thanks')

]
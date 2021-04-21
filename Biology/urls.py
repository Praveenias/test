from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.biology,name='biology'),
    path('thank',views.thank,name='thanks')

]
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('travel/', travel, name="travel"),
    path('camping/', camping, name="camping"),
    path('exercise/', exercise, name="exercise"),
    path('study/', study, name="study"),
    path('cultural/', cultural, name="cultural"),
    path('explanation/',explanation, name="explanation"),
]
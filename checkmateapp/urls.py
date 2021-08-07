from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('detail/<str:post_id>', detail, name ="detail"),
    path('new/', new, name = "new"),
    path('edit/<str:post_id>', edit, name = "edit"),
    path('delete/<str:post_id>', delete, name = "delete"),
    path('search/', search, name='search'),
]
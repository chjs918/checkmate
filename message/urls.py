from django.urls import path
from .views import *   

app_name = 'message'

urlpatterns = [   
    path('receive_box/', receive_box, name="receive_box"),
    path('send_box/', send_box, name="send_box"),
    path('<str:id>', detail_message, name="detail_message"),  
    path('new_message/<str:post_id>', new_message, name="new_message"),
]
from django.urls import path
from .views import chat_func, room

app_name = 'chat'

urlpatterns = [
    path('', chat_func, name = 'chat'),
    path('/<str:room_name>/', room, name='room'),
]

from django.urls import path, include
from . import views
from chat.views import chat_func
urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('friends', views.friends, name='friends'),
    path('users', views.users, name='users'),
    path('messages', views.messages, name='messages'),
    path('login', views.loginPage, name='login'),
    path('register', views.registerPage, name='register'),
    path('logout', views.logoutUser, name='logout'),
    path('register_form', views.register_form, name='register_form'),
    path('chat', include('chat.urls', namespace='chat')),
]

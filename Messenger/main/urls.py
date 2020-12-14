
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('friends', views.friends, name='friends'),
    path('users', views.users, name='users'),
    path('messages', views.messages, name='messages'),
    path('login', views.loginPage, name='login'),
    path('register', views.registerPage, name='register'),
    path('logout', views.logoutUser, name='logout'),
    path('register_form', views.register_form, name='register_form')
]

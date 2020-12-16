from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('about-us/', about, name='about'),
    path('create/', create, name='create'),
]

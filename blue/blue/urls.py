from django.contrib import admin
from django.urls import path, include
#from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    #path('accounts/', include('allauth.urls'))#10
    #path('login/', user_login, name='login'),
    #path('', views.),
]
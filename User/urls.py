
from django.urls import path
from .views import register, Logout, login

app_name='User'

urlpatterns = [
    path('register/', register, name = 'register'),
    path('logout/', Logout, name = 'logout'),
    path('login/', login, name = 'login'),
    

]
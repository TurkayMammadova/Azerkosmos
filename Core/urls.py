
from django.urls import path
from .views import index

app_name='Core'

urlpatterns = [
    path('index/', index, name = 'index'),
  
]

from django.urls import path
from .views import index,detail,departments

app_name='Core'

urlpatterns = [
    path('departments/',departments,name='departments'),
    path('detail/<int:id>',detail,name='detail'),
   
]
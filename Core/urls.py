
from django.urls import path
from .views import departments,detail

app_name='Core'

urlpatterns = [
    path('departments/',departments,name='departments'),
    path('detail/<int:id>',detail,name='detail'),
    # path('table_detail/<int:id>',table_detail,name='table_detail'),
   
]
from django.urls import path
from app2.views import *
app_name='nothing2'
 

urlpatterns=[
    path('Hi/',Hi,name='Hi')
]
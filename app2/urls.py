from django.urls import path
from app2.views import *
app_name='anything2'
urlpatterns = [
    path('jinjaprint2',jinjaprint2,name='jinjaprint2'),
]
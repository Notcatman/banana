from django.urls import path 
from .views import *

urlpatterns = [
    path('', list, name='tasks'),
    path("task/<int:id>", detail, name='detail_page')
]
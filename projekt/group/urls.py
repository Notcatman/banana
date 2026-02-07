from django.urls import path 
from .views import *

urlpatterns = [
    path('', list, name='tasks'),
    path("task/<int:id>", detail, name='detail_page'),
    path('add/', add_task, name='add_task'),
    path("delete/<list_id>", delete, name="delete"),
    path("cross/<list_id>", cross, name="cross"),
    path("uncross/<list_id>", uncross, name="uncross"),
    path('edit/<int:id>', edit, name='edit')
]
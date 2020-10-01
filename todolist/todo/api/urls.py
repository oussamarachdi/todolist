from django.urls import path
from .views import ListDetail, ListCreate, ItemDetail, ItemCreate

urlpatterns = [
    path('ld/<id>/', ListDetail.as_view(), name='list-rud'),
    path('lc/', ListCreate.as_view(), name='list-create'),
    path('di/<id>/', ItemDetail.as_view(), name='Item-rud'),
    path('ic/', ItemCreate.as_view(), name='Item-create'),
]
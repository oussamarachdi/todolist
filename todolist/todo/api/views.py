from todo.models import List, Item
from .serializers import ListGetSerializer, ListCreateSerializer, ItemGetSerializer, ItemCreateSerializer
from rest_framework import generics

class ListCreate(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListCreateSerializer


class ListDetail(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'id'
	queryset = List.objects.all()
	serializer_class = ListGetSerializer

class ItemCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemCreateSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'id'
	queryset = Item.objects.all()
	serializer_class = ItemGetSerializer
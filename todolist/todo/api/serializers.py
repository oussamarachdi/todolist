from rest_framework import serializers
from todo.models import List, Item

class ListGetSerializer(serializers.Serializer):
	class Meta:
		model = List

		feilds = [
			'id',
			'name'
		]

class ListCreateSerializer(serializers.Serializer):
	class Meta:
		model = List
		feilds = '__all__'		

class ItemGetSerializer(serializers.Serializer):
	class Meta:
		model = Item
		feilds = [
			'id',
			'name',
			'date'
		]

class ItemCreateSerializer(serializers.Serializer):
	class Meta:
		model = Item
		feilds = [
			'id',
			'name',
			'isdone',
			'date'
		]	
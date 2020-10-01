from django.db import models
from .list import List 


class Item(models.Model):
	listname = models.ForeignKey(List, on_delete=models.CASCADE)
	name = models.CharField(max_length = 60)
	isdone = models.BooleanField(default = False)
	date = models.CharField(max_length=20)

	def __str__(self):
		return self.name
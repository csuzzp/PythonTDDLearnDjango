from django.db import models
#from django.db.utils import lists_list
# Create your models here.

class List(models.Model):
	pass
	
class Item(models.Model):
	text = models.TextField(default='')
	list = models.ForeignKey(List,default=None)

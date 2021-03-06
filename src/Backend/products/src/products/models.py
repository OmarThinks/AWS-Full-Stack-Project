from django.db import models
from django.core.validators import (MaxValueValidator, MinValueValidator)



#id,name,price,in_stock
class Product(models.Model):
	name = models.CharField(max_length=150)
	price = models.FloatField(
		validators=[MinValueValidator(.1),MaxValueValidator(1000*1000)])
	in_stock =  models.BooleanField()

	def __str__(self):
		return (str(self.id) +") "+ self.name + ", "+ str(self.author))


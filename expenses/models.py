from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Member(models.Model):
	name=models.CharField(max_length=250)

	def __str__(self):
		return self.name

class Category(models.Model):
	name=models.CharField(max_length=250)

class Expense(models.Model):
	comment=models.TextField(blank=True, null=True)
	datetime=models.DateTimeField(default=datetime.now)
	amount=models.DecimalField(decimal_places=2,max_digits=20)
	user = models.ForeignKey(Member, on_delete=models.PROTECT)




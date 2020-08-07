from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

# Create your models here.

class profile(models.Model):
	user = models.OneToOneField(User , on_delete = models.CASCADE)
	name = models.CharField(max_length = 20 , blank= False)
	email = models.EmailField(max_length=100)

	def __str__(self):
		return self.name


class event(models.Model):
	user = models.ForeignKey(User , on_delete = models.CASCADE)
	date  = models.DateField(default=datetime.now())
	time = models.TimeField(blank = True , default=timezone.now())
	details = models.TextField(max_length=200)

	def __str__(self):
		return str(self.date) 
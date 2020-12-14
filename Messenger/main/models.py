from django.db import models


class UserInfo(models.Model):

	username = models.CharField(max_length=100, default = "SomeString")
	age = models.IntegerField()
	first_name = models.CharField(max_length = 200)
	last_name = models.CharField(max_length = 200)
	job = models.CharField(max_length = 200)


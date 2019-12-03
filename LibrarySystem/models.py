from django.db import models

# Create your models here.

class User(models.Model):
	user_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=50, blank=True)
	password = models.CharField(max_length=50)
	mobile_no = models.IntegerField()
	address = models.CharField(max_length=60)

	def __str__(self):
		return self.name


class Book(models.Model):
	book_id = models.IntegerField(primary_key=True)
	book_type = models.CharField(max_length=30)
	book_price = models.IntegerField()
	available = models.BooleanField(default=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	issue_date = models.DateField()
	expiry_date = models.DateField()
	renewal_date = models.DateField()
	author_name = models.CharField(max_length=25)
	publication_date = models.DateField()

	def __str__(self):
		return self.name

class Search_Book(models.Model):
	s_id = models.IntegerField(primary_key=True)






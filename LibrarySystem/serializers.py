from rest_framework import serializers
from .models import User, Book, Search_Book

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('user_id', 'name', 'email', 'password', 'mobile_no', 'address')


class BookSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Book
		fields = ('book_id', 'book_type', 'book_price', 'available', 'user', 'issue_date', 'expiry_date', 'renewal_date', 'author_name', 'publication_date')


class Search_BookSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Search_Book
		fields = ('s_id')
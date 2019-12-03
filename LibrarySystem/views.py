from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import User, Book, Search_Book 
from .serializers import UserSerializer, BookSerializer, Search_BookSerializer

# Create your views here.

class UserView(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class BookView(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class Search_BookView(viewsets.ModelViewSet):
	queryset = Search_Book.objects.all()
	serializer_class = Search_BookSerializer
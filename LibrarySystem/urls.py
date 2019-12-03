from django.urls import path, include
from .import views
from rest_framework import routers
 

router = routers.DefaultRouter()
router.register('users', views.UserView)
router.register('books', views.BookView)
router.register('search_books', views.Search_BookView)

urlpatterns = [

path('', include(router.urls))

]

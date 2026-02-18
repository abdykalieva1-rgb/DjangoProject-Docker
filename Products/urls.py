
from django.urls import path
from .views import products,next_page
urlpatterns = [
    path('',products),
    path('next_page/',next_page,name='next_page'),
]

from django.urls import path
from .views import Products, next_page, second_page

urlpatterns = [
    path('', Products, name='product'),
    path('next_page/', next_page, name='next_page'),
    path('second_page/<int:id>/', second_page, name='second_page'),


]
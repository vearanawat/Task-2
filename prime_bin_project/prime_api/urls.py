from django.urls import path
from .views import prime_binary

urlpatterns = [
    path('prime_binary/', prime_binary, name='prime_binary'),
]
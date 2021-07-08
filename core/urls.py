from django.urls import path

from core.views import index, generate_password

urlpatterns = [
    path('', index),
    path('generate-password/', generate_password, name='generate-password')
]
from .api import proyecto_api_view
from django.urls import path

urlpatterns = [
    path('proyecto/', proyecto_api_view, name='proyecto_api_view')
]
from .api import tarea_api_view
from django.urls import path

urlpatterns = [
    path('tarea/', tarea_api_view, name='tarea_api_view')
]
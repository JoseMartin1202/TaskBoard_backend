from .api import test_api_view
from django.urls import path

urlpatterns = [
    path('admin/', test_api_view,name='test_api_view')
]

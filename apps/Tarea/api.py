from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser,  JSONParser
from .models import Tarea
from .serializers import TareaSerializer

@api_view(['POST'])
@parser_classes([MultiPartParser , JSONParser])
def tarea_api_view(request):
    if request.method == 'POST':
        tareaSerializer = TareaSerializer(data=request.data)
        if tareaSerializer.is_valid():
            tareaSerializer.save()
            return Response(tareaSerializer.data, status=status.HTTP_201_CREATED)
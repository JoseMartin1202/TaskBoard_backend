from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser,  JSONParser
from .models import Proyecto
from .serializers import ProyectoSerializer

@api_view(['GET','POST'])
@parser_classes([MultiPartParser , JSONParser])
def proyecto_api_view(request):
    if request.method == 'GET':
        proyectos = Proyecto.objects.all()
        proyectos_serializer = ProyectoSerializer(proyectos, many=True)
        return Response(proyectos_serializer.data, status=status.HTTP_200_OK)
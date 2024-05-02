from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, JSONParser
from .models import Test
from .serializers import TestSerializer

@api_view(['POST'])
@parser_classes([MultiPartParser, JSONParser])
def test_api_view(request):
    if request.method == 'POST':
        test_serializer = TestSerializer(data=request.data)
        if test_serializer.is_valid():
            test_serializer.save()
            return Response(test_serializer.data, status=status.HTTP_201_CREATED)

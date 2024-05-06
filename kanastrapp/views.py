#from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Person
from .serializers import PersonSerializer
from rest_framework import status
import logging


# Create your views here.

logger = logging.getLogger(__name__)

@api_view(['GET'])
def getPeople(request):
    people = Person.objects.all()
    serializer = PersonSerializer(people, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addPerson(request):
    serializer = PersonSerializer(data=request.data)

    if serializer.is_valid():
        try:
            serializer.save()
            logger.info(f'Dados salvos com sucesso: {serializer.data}')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(f'Erro ao executar a operação: {str(e)}')
            return Response({'Erro': 'Erro ao salvar os dados'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
       logger.warning(f'Dados recebidos são inválidos: {serializer.errors}')
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
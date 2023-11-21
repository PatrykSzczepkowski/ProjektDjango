from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Osoba,Stanowisko
from .serializers import OsobaModelSerializer, StanowiskoModelSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the polls index. <33333")

#wyswietlanie obiektow Osoba
@api_view(['GET'])
def osoba_list(request):
    if request.method == 'GET':
        osoby = Osoba.objects.all()
        serializer = OsobaModelSerializer(osoby, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def osoba_list_str(request, znaki):
    if request.method == 'GET':
        osoby = Osoba.objects.filter(nazwisko__contains=znaki)
        if osoby.exists():
            serializer = OsobaModelSerializer(osoby, many=True)
            return Response(serializer.data)
        else:
            return  Response("Nie znaleziono żadnej osoby z podanym nazwiskiem.", status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'PUT', 'DELETE'])
def osoba_detail(request,pk):
    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Person
    :return: Response (with status and/or object/s data)
    """
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        osoba = Osoba.objects.get(pk=pk)
        serializer = OsobaModelSerializer(osoba)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OsobaModelSerializer(osoba , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def stanowisko_detail(request,pk):
    try:
        stanowisko = Stanowisko.objects.get(pk=pk)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        stanowisko = Stanowisko.objects.get(pk=pk)
        serializer = OsobaModelSerializer(stanowisko)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OsobaModelSerializer(stanowisko , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stanowisko.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def stanowisko_list(request):
    if request.method == 'GET':
        stanowiska = Stanowisko.objects.all()
        serializer = StanowiskoModelSerializer(stanowiska, many=True)
        return Response(serializer.data)


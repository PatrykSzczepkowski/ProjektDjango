from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response
from .models import Osoba,Stanowisko
from .serializers import OsobaModelSerializer, StanowiskoModelSerializer
from django.core.exceptions import PermissionDenied

def index(request):
    return HttpResponse("Hello, world. You're at the polls index. <33333")

def osoba_view(request, pk):
    if not request.user.has_perm('polls.view_Osoba'):
        raise PermissionDenied()
    try:
        osoba = Osoba.objects.get(pk=pk)
        if osoba.wlasciciel == request.user or request.user.has_perm('polls.can_view_other_persons'):
            return HttpResponse(f"Ten użytkownik nazywa się {osoba.imie} {osoba.nazwisko}")
    except Osoba.DoesNotExist:
        return HttpResponse(f"W bazie nie ma użytkownika  o id={pk}.")


#wyswietlanie obiektow Osoba
@api_view(['GET'])
@login_required
def osoba_list(request):
    if request.method == 'GET':
        # Filtruj obiekty Osoba, aby wyświetlić tylko te, które należą do zalogowanego użytkownika
        osoby = Osoba.objects.filter(wlasciciel=request.user)
        serializer = OsobaModelSerializer(osoby, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([DjangoModelPermissions])
def osoba_list_str(request, znaki):
    if request.method == 'GET':
        osoby = Osoba.objects.filter(nazwisko__contains=znaki)
        if osoby.exists():
            serializer = OsobaModelSerializer(osoby, many=True)
            return Response(serializer.data)
        else:
            return  Response("Nie znaleziono żadnej osoby z podanym nazwiskiem.", status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def osoba_detail(request,pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        osoba = Osoba.objects.get(pk=pk)
        serializer = OsobaModelSerializer(osoba)
        return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([DjangoModelPermissions])
def osoba_update(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = OsobaModelSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def osoba_delete(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
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


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def stanowisko_members(request, pk):
    try:
        stanowisko = Stanowisko.objects.get(pk=pk)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        osoby = Osoba.objects.filter(stanowisko=stanowisko)
        serializer = OsobaModelSerializer(osoby, many=True)
        return Response(serializer.data)
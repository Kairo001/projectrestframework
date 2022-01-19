""" Vistas de usuarios. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Serializers
from cride.users.serializers import (
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer,
    AccountVerificationSerializer
)
    

class UserLoginAPIView(APIView):
    """ Vista de la API de login de usuario. """
     
    def post(self, request, *args, **kwargs):
        """ Manejador de la petición POST de http. """
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)
    
class UserSignUpAPIView(APIView):
    """ Vista de la API de signup de usuario. """
     
    def post(self, request, *args, **kwargs):
        """ Manejador de la petición POST de http. """
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED) 

class AccountVerificationAPIView(APIView):
    """ Vista de la API para verificación de cuenta. """

    def post(self, request, *args, **kwargs):
        """ Manejador de la petición POST de http. """
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': '¡Felicidades, tu cuenta ha sido verificada!'}
        return Response(data, status=status.HTTP_200_OK) 
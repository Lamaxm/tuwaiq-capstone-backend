from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import AccessToken,Token
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import UserRegisterSerializer



@api_view(['POST'])
def login_user(request : Request):

    if 'username' in request.data and 'password' in request.data:
        user = authenticate(request, username=request.data['username'], password=request.data['password'])
        if user is not None:
            #create the token , then give the token to the user in the response
            token = AccessToken.for_user(user)
            responseData = {
                "msg" : "Your token is ready",
                "token" : str(token)
            }
            return Response(responseData)


    return Response({"msg" : "please provide your username & password"}, status=status.HTTP_401_UNAUTHORIZED)


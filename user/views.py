from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import AccessToken



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


    return Response({"msg" : "please provide your username or password"}, status=status.HTTP_401_UNAUTHORIZED)


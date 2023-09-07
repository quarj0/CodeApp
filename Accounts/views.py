"""
This file is used to create views for the Accounts for the registration and login of the user.
"""
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, LoginSerializer


# Register API
class RegisterAPI(generics.GenericAPIView):
    """
    This class is used to register the user.
    """
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        """
        This method is used to register the user.
        :param request: It is used to get the request from the user.
        :param args: It is used to get the arguments.
        :param kwargs: It is used to get the keyword arguments.
        :return: It returns the response.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,
                                   context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
        

# Login API
class LoginAPI(generics.GenericAPIView):
    """
    This class is used to login the user.
    """
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        """
        This method is used to login the user.
        :param request: It is used to get the request from the user.
        :param args: It is used to get the arguments.
        :param kwargs: It is used to get the keyword arguments.
        :return: It returns the response.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        _, token = AuthToken.objects.create(user)
        return Response({
            "user": UserSerializer(user,
                                   context=self.get_serializer_context()).data,
            "token": token
        })
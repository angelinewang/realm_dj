from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt

# Retrieve User model
User = get_user_model()
# Default user model from Django Admin

# Class based views for User Authentication

class RegisterView(APIView):
    # Signup Page
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration Successful'})
        return Response(serializer.errors, status=422)

class LoginView(APIView):
    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise PermissionDenied({'message': 'Invalid Credentials!'})

    # Login Page
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = self.get_user(email)
        if not user.check_password(password):
            raise PermissionDenied({'message': 'Invalid Credentials!'})

        token = jwt.encode(
            {'sub': user.id},
            settings.SECRET_KEY,
            algorithm='HS256'
        )

        return Response({'token': token, 'message': f'Welcome back {user.username}!!'})

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAdminUser | IsAuthorOrReadOnly,)
    # Comma says that this is a Tuple, but there is only one item -- Tuples are iterable and things in parentheses are not iterable -- If just parentheses without a comma: Then think you are just using then to tidy up code, does not know it is a Tuple

class GuestsList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

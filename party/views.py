from django.shortcuts import render
from rest_framework import generics
from .models import Party
from .serializers import PartySerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from user.serializers import UserRoleSerializer
from user.authentication import JWTAuthentication

# Create your views here.

class PartyPost(generics.CreateAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    serializer_class = PartySerializer
    # Checks that user is logged in 
    # authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):

        serializer = PartySerializer(data=request.data)

        User = get_user_model().objects.get(id=request.user.id)

        roleSerializer = UserRoleSerializer(User, data=request.data)
        if serializer.is_valid():
            # Passing authenticated user id as foreign key
            serializer.save(host=request.user)
            if roleSerializer.is_valid():
                roleSerializer.save(role=1)
            return Response({'message': 'Party Posted'})
        return Response(serializer.errors, status=422)



# Invites page
# Confirmed page
# Guestlist page

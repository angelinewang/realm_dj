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
from django.shortcuts import HttpResponse, get_object_or_404, get_list_or_404
from django.core.exceptions import PermissionDenied

from party.serializers import PartySerializer, PartyIdSerializer

class MyPartiesView(generics.ListAPIView):
    serializer_class = PartyIdSerializer
 
    def get_queryset(self, *args, **kwargs):
        # From the Host User ID, get the Party, and return just the party id 
        pk = self.kwargs.get('pk')
        parties = Party.objects.filter(host_id=pk).order_by('created_at')
        
        # Send all my parties and pick out the final one through frontend 

        return parties

class PartyPost(generics.CreateAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    serializer_class = PartySerializer
    # Checks that user is logged in 
    # authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):

        serializer = PartySerializer(data=request.data)

        pk = self.kwargs.get('pk')
        User = get_user_model().objects.get(id=pk)

        # User = get_user_model().objects.get(id=request.user.id)

        roleSerializer = UserRoleSerializer(User, data=request.data)

        # If User role is currently set to Host, raise exception that permission is denied 
        if User.role == 1:
            raise PermissionDenied() 
            # 403 Forbidden
     
        elif serializer.is_valid():
            # Passing authenticated user id as foreign key
            # serializer.save(host=request.user)
            serializer.save(host=User)
            if roleSerializer.is_valid():
                roleSerializer.save(role=1)
            return Response({'message': 'Party Posted'})

        return Response(serializer.errors, status=422)

# WORKING 
# 1. Grabs the User_id from the url
# 2. Finds all the parties whose host_id is the user_id
# 3. Returns the last/most recent party 

# Invites page
# Confirmed page
# Guestlist page

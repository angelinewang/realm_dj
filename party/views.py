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

# Create your views here.

class PartyPost(generics.CreateAPIView, mixins.CreateModelMixin):
    serializer_class = PartySerializer
    # Checks that user is logged in 
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        current_user = request.user.id
        serializer = PartySerializer(data=request.data, user=current_user)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Party Posted'})
        return Response(serializer.errors, status=422)

    # def post(self, request, *args, **kwargs):
    #     return Party.objects.create(self)
    #     # request.user.id = host_id
# Invites page
# Confirmed page
# Guestlist page

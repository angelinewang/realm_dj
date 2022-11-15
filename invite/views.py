from django.shortcuts import render
from rest_framework import generics
from .models import Invite
from .serializers import InviteSerializer
from rest_framework import mixins
from rest_framework import permissions

# Create your views here.

class PartiesList(generics.ListAPIView):
    queryset = Invite.objects.all()
    serializer_class = InviteSerializer

class CreateInvite(generics.CreateAPIView, mixins.UpdateModelMixin, mixins.CreateModelMixin):
    queryset = Invite.objects.all()
    serializer_class = InviteSerializer
    # Checks that user is logged in 

    # Create a permissions file, and add IsHost
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return Invite.objects.create(self, request, *args, **kwargs)
    
    # PUT is used to replace all current properties

    # PATCH is used to modify only some parts of the object

    # The following endpoint is used ONLY to change the "status" property of an Invite object
    def patch(request, *args, **kwargs):
            return Invite.objects.partial_update(request, *args, **kwargs)
# Invites page
# Confirmed page
# Guestlist page
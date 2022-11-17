from django.shortcuts import render
from rest_framework import generics
from .models import Invite
from .serializers import InviteSerializer
from rest_framework import mixins
from rest_framework import permissions
from django.core.exceptions import PermissionDenied
from .serializers import SendInviteSerializer
from rest_framework.response import Response
from .serializers import UpdateInviteSerializer
from .models import Party
from user.authentication import JWTAuthentication
from django.contrib.auth import get_user_model

# Create your views here.

class PartiesList(generics.ListAPIView):
    queryset = Invite.objects.all()
    serializer_class = InviteSerializer
    # authentication_classes = [JWTAuthentication]

class CreateInvite(generics.CreateAPIView, mixins.UpdateModelMixin, mixins.CreateModelMixin):
    queryset = Invite.objects.all()
    serializer_class = SendInviteSerializer
    # Checks that user is logged in 

    # Create a permissions file, and add IsHost
    # authentication_classes = [JWTAuthentication]

    # 1. Is Host 2. Grab Party Associated

    def post(self, request, *args, **kwargs):

        # Create invite where the party id is the party of the host
        # And the guest_id is the id in the API URL

        serializer = SendInviteSerializer(data=request.data)
        
        if request.user.role == 1 and serializer.is_valid():
            # Passing authenticated user id as foreign key
            serializer.save(party_id=Party.objects.get(host_id=request.user.id), guest_id=get_user_model().objects.get(id=object_id))
            return Response({'message': 'Invite Sent'})

            return Response(serializer.errors, status=422)

            # return Invite.objects.create(self, request, *args, **kwargs)
        else:
            raise PermissionDenied()
    
    # PUT is used to replace all current properties

    # PATCH is used to modify only some parts of the object

    # The following endpoint is used ONLY to change the "status" property of an Invite object

class ConfirmInvite(generics.UpdateAPIView):
    # authentication_classes = [JWTAuthentication]
    def patch(request, *args, **kwargs):
        invite = Invite.objects.get(id=request.data.id)
        serializer = UpdateInviteSerializer(invite, data=request.data)

        if serializer.is_valid:
            serializer.save(status=1)
            return Response({'message': 'Guest Confirmed'})
        return Response(serializer.errors, status=422)

class CancelInvite(generics.UpdateAPIView):
    # authentication_classes = [JWTAuthentication]
    def patch(request, *args, **kwargs):
        invite = Invite.objects.get(id=request.data.id)
        serializer = UpdateInviteSerializer(invite, data=request.data)

        if serializer.is_valid:
            serializer.save(status=2)
            return Response({'message': 'Guest Confirmed'})
        return Response(serializer.errors, status=422)

class CheckinInvite(generics.UpdateAPIView):
    # authentication_classes = [JWTAuthentication]

    def patch(request, *args, **kwargs):
        invite = Invite.objects.get(id=request.data.id)
        serializer = UpdateInviteSerializer(invite, data=request.data)

        if serializer.is_valid:
            serializer.save(status=3)
            return Response({'message': 'Guest Confirmed'})
        return Response(serializer.errors, status=422)


# Invites page
# Confirmed page
# Guestlist page
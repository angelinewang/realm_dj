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
from .serializers import HostSerializer, GuestSerializer
from .serializers import PartySerializer
from django.views.generic import DetailView
from django.shortcuts import HttpResponse, get_object_or_404, get_list_or_404
from django.http import Http404
from rest_framework.decorators import api_view

# Create your views here.

class PartiesInvitedList(generics.ListAPIView):
    serializer_class = InviteSerializer

    def get_queryset(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        return get_list_or_404(Invite, status=0, guest_id=pk)

class HostView(generics.RetrieveAPIView):
    serializer_class = HostSerializer
    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        return get_object_or_404(get_user_model(), id=pk)

class PartyView(generics.RetrieveAPIView):
    serializer_class = PartySerializer
    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Party, id=pk)

class PartiesConfirmedList(generics.ListAPIView):
    serializer_class = InviteSerializer

    def get_queryset(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        return get_list_or_404(Invite, status=1, guest_id=pk)

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

# WORKING 
# Grabs the Party_id from the URL
# Lists the Invites with the Party_id
class GuestlistInvites(generics.ListAPIView):
    serializer_class = InviteSerializer

    def get_queryset(self, *args, **kwargs):
    # From the Host User ID, get the Party, then get the invites from the Party 
        pk = self.kwargs.get('pk')
        parties = Party.objects.filter(host_id=pk)
        myParty = parties.order_by('created_at').last()
        return get_list_or_404(Invite, party_id=myParty.id)

# Grabs the User_id from the URL
# Retrieves the User Profile with the id equivalent
class GuestlistGuest(generics.RetrieveAPIView):
    serializer_class = GuestSerializer

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        return get_object_or_404(get_user_model(), id=pk)

    # User party is grabbed from the frontend, because when calling the guestlist page, need the party ID

# Grab the party by the current user first

# From the party, grab the invites

# From the invites, grab the invites that are confirmed

# From the confirmed invites, grab the guests from the invites 

# Render the guest profiles from the invites 

    # authentication_classes = [JWTAuthentication]


# Serialiser the Guest Profile, from the invite (which has a certain party id, which is tied to the user/host)
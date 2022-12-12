from django.shortcuts import render
from rest_framework import generics
from .models import Invite
from .serializers import InviteSerializer
from rest_framework import mixins
from rest_framework import permissions
from django.core.exceptions import PermissionDenied
from .serializers import CreateInviteSerializer
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
from datetime import datetime, timedelta
import pytz

utc = pytz.UTC
# Create your views here.

class PartiesInvitedList(generics.ListAPIView):
    serializer_class = InviteSerializer
    # serializer_class = PartySerializer

    def get_queryset(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        
        # Get all invites whose guest_id is the same as the authUser
        # Filter the parties so that only the ones with last entry in the future are shown

        # This should return all 5 parties Bob is invited to: 3 in the future and 2 in the past
        # return get_list_or_404(Invite, status=0, guest_id=pk) WORKING 

        invitedParties = get_list_or_404(Invite, status=0, guest_id=pk)

        # 1. Add a few invites for Bob: 3 in future, 2 in past
        # 2. Try API Endpoint on Postman again 

        partiesIds = []

        for v in invitedParties:
            partiesIds.append(v.party_id_id)
            print(partiesIds)

        # Get the parties whose id is in invitedParties 

        # return Party.objects.filter(id__in=partiesIds) 
        # return Party.objects.filter(id__in=partiesIds)
        
        parties = Party.objects.filter(id__in=partiesIds)

        # datetime.now() is "aware": It has reference to UTC time zone in the end
        naiveNow = datetime.now()


        # first_entry is "naive"

        # lastEntries returns a list of party ids for the Invites
        # from the list of party ids, return all parties from "parties" that have a party_id_id within lastEntries
        lastEntries = []

        for v in parties:
            print("FIRST ENTRY:")
            print(v.first_entry)

            last_entry = v.first_entry + timedelta(hours=12)

            print("LAST ENTRY:")
            print(last_entry)

            awareNow = utc.localize(naiveNow)
            print("NOW:")
            print(awareNow)

            # Changed "now" from "naive" to "aware"
            if last_entry < awareNow:
                print("Last Entry is in the PAST")
                print("This Party's Last Entry has passed")
                print(lastEntries)
                    # If last entry has passed
                    # Append this party into the list of returned parties
            
            elif last_entry > awareNow:
                        # If last entry is is still in future: Do not change the user role and return the user data as is
                print("Last Entry is the FUTURE")
                lastEntries.append(v.id)
                print(lastEntries)
        
        futureInvites = []

        for v in invitedParties:
            if v.party_id_id in lastEntries:
                futureInvites.append(v)
                
        # Returns the list of invites belonging to the user filtered to only include invites with party ids that have been determined to be in the future
        return futureInvites
        
        # 1. Find all the invites 
        # 2. Create a list of the parties with ID and first entry 
        # 3. Amend the list so that the first entry is changed into the last entry 
        # 4. Delete irrelevant parties from list 
        # 5. Use IDs the parties remaining to get the list of party invites for the User
        # 6. Return this list has the list of invites 

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

class CreateInvite(generics.CreateAPIView):
    # Only users able to reach the CreateInvite view are ALREADY determined to be Host
    # Role of User validated on frontend
    # If User is a Guest, they will be brought to Add Party Modal 

    queryset = Invite.objects.all()
    serializer_class = CreateInviteSerializer

    # Flow of Invite Creation:
    # 1. Frontend: Determine if User is Host 
    # 2. Frontend: Get Party associated with User --> With authUserId in URL Parameters
    # 3. Backend: Call CreateInvite API with Guest Id & Party Id as fields in body of the anonymous call
    # Since Party automatically associated with Host Id, no need to pass Id of authenticated User when making POST Request

    # CreateInviteView works, but occasionally begins data creation with existing IDs
    # Continual retry of Invite Creation overcomes this issue
    def post(self, request, *args, **kwargs): 
        # 2 Variables needed for creating invite:
        # #1 Party ID ---> Through body of request
        # #2 Guest ID ---> Through URL parameter

        serializer = CreateInviteSerializer(data=request.data)

        # User Role validated as Host through frontend
        if serializer.is_valid():
            # Passing authenticated user id as foreign key
            serializer.save()
            return Response({'message': 'Invite Created'})

        return Response(serializer.errors, status=422)

            # return Invite.objects.create(self, request, *args, **kwargs)
        # else:
        #     raise PermissionDenied()
    
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
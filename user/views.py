from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import UserSerializer
from .serializers import UserLoginSerializer
from .serializers import UserProfileSerializer, UserRoleSerializer, UserSignUpSerializer, FirstEntrySerializer, UpdatePhotoSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt
from rest_framework import mixins
from rest_framework import permissions
from  user.authentication import JWTAuthentication
from django.shortcuts import get_list_or_404, get_object_or_404
from party.models import Party 
from invite.models import Invite
from invite.serializers import InviteSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files import File
import urllib 

from storages.backends.gcloud import GoogleCloudStorage
storage = GoogleCloudStorage()

from datetime import datetime, timedelta
import pytz

utc=pytz.UTC
# Retrieve User model
User = get_user_model()
# Default user model from Django Admin

# Class based views for User Authentication


class RegisterView(generics.CreateAPIView):
    # Signup Page
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser, FormParser)

    # permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)

        # Checks if a row of data with the same email already exists in the database
        # UNIQUE Constraint added to the "email" column of user_customuser table
        # If email entered already exists, will through Error: "Key (email)=(testing@kcl.ac.uk) already exists."
        # print(request.data.get('email'))
        # profile_picture = request.data.get('profile_picture')
        email = request.data.get('email')

        # target_path = 'images' + email
        # path = storage.save(target_path, profile_picture)

        # profile_picture_data = storage.url(path)
        profile_picture = request.FILES['profile_picture']
        # profile_picture_data = User.Upload.upload_image(profile_picture, profile_picture.name)
        
        password = request.data.get('password')
        birthdate = request.data.get('birthdate')
        department = request.data.get('department')
        gender = request.data.get('gender')
        name = request.data.get('name')

        print(profile_picture)
        # print(profile_picture_data)
        print(email)
        print(password)
        print(birthdate)
        print(department)
        print(gender)
        print(name)

        # Birthdate must be in the format: YYYY-MM-DD

        # user = self.get_user(email)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration Successful'})
        return Response(serializer.errors, status=422)

class LoginView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
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

class UpdatePhoto(generics.RetrieveUpdateDestroyAPIView, mixins.UpdateModelMixin):
    serializer_class = UpdatePhotoSerializer
    parser_classes = (MultiPartParser, FormParser)
    queryset = get_user_model().objects.all()

    def patch(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        get_user_model().objects.filter(id=pk).update(profile_picture=request.data.get('profile_picture'))
            #     if serializer.is_valid():
            # serializer.save()
            # return Response({'message': 'Registration Successful'})
        return Response("Profile Photo Updated!")

class FirstEntryView(generics.RetrieveUpdateDestroyAPIView, mixins.UpdateModelMixin):
    # 1. Grab the last party associated to the user 
    # 2. Use the FirstEntrySerialiser to only send back the first entry of the party 
    # 3. Respond with True or False of last entry being over 
    serializer_class = FirstEntrySerializer
    def get(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        parties = Party.objects.filter(host_id=pk)
        myParty = parties.order_by('created_at').last()

        naiveNow = datetime.now() # datetime.now() is "aware": It has reference to UTC time zone in the end

        # first_entry is "naive"
        last_entry = myParty.first_entry + timedelta(hours=12)
        print("FIRST ENTRY:")
        print(myParty.first_entry)
        print("LAST ENTRY:")
        print(last_entry)

        # Changed "now" from "naive" to "aware"
        awareNow = utc.localize(naiveNow)
        print("NOW:")
        print(awareNow)

        if last_entry < awareNow:
            passed_last_entry = True 
        # If last entry has passed
            return Response(passed_last_entry)
        elif last_entry > awareNow:
            # If last entry is is still in future: Do not change the user role and return the user data as is
            passed_last_entry = False
            return Response(passed_last_entry)

class RoleChangeView(generics.RetrieveUpdateDestroyAPIView, mixins.UpdateModelMixin):
    
    serializer_class = UserRoleSerializer
    def get_queryset(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        get_user_model().objects.filter(id=pk).update(role=0)

        return get_user_model().objects.filter(id=pk)

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView, mixins.UpdateModelMixin):
    # authentication_classes = [JWTAuthentication]

    # Before sending user details back in response: Check is the user's role is Host. 
    # If yes, check the last party with host_id of the user. 
    # Then check if the first_entry of that party is more than 12 hours ahead of current time 
    # If yes, then change the user role to Guest. 

    # queryset = User.objects.all()
    # <int:pk> set at the URL automatically means this View only gets one profile: That of the user indicated
    # Do not need to specify it inside this class

    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    # def get_queryset(self, *args, **kwargs):

    #     pk = self.kwargs.get('pk')
    #     return get_object_or_404(get_user_model(), id=pk)

        # serializer = UserProfileSerializer(data=User)

        # if serializer.is_valid() and User.role == 1: 
        #     # Find Party 
        #     parties = Party.objects.filter(host_id=pk)
        #     myParty = parties.order_by('created_at').last()
        #     # Check time of Party
        #     naiveNow = datetime.now() # datetime.now() is "aware": It has reference to UTC time zone in the end
    
        #     # first_entry is "naive"
        #     last_entry = myParty.first_entry + timedelta(hours=12)
        #     print("FIRST ENTRY:") 
        #     print(myParty.first_entry)
        #     print("LAST ENTRY:")
        #     print(last_entry)

        #     # Changed "now" from "naive" to "aware"
        #     awareNow = utc.localize(naiveNow)
        #     print("NOW:")
        #     print(awareNow)

        #     if last_entry < awareNow:
        #     # If last entry has passed
        #         # roleSerializer = UserRoleSerializer(User, data=User)
        #         if serializer.is_valid():
        #             serializer.save(role=0)
        #             return Response({'message': 'Role Changed'})
        #             return get_object_or_404(get_user_model(), id=pk)
        #     elif last_entry > awareNow:
        #         # If last entry is is still in future: Do not change the user role and return the user data as is
        #         return get_object_or_404(get_user_model(), id=pk)
            
        # elif User.role == 0:
        #     # If user role is guest, just return the User Info as present
        #     return get_user_model().objects.get(id=pk)
            # Change the user role to guest, and post it to the backend
            # Before sending back to the frontend the profile details

        # 1. Change the user Role 
        # 2. Return User Profile



    # permission_classes = (permissions.IsAdminUser | IsAuthorOrReadOnly,)
    # Comma says that this is a Tuple, but there is only one item -- Tuples are iterable and things in parentheses are not iterable -- If just parentheses without a comma: Then think you are just using then to tidy up code, does not know it is a Tuple
    # def patch(request, *args, **kwargs):
    #     return User.objects.partial_update(request, *args, **kwargs)

class GuestsBrowseGuestMode(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self, *args, **kwargs):
        pk = self.kwargs.get('pk')

        return User.objects.exclude(id=pk)
        # print(User.objects.get(id=pk).role)
        
        # role = User.objects.get(id=pk).role
        # if role == 0:

class ExistingInvitesView(generics.ListAPIView):
    serializer_class = InviteSerializer
    def get_queryset(self, *args, **kwargs):
        party = self.kwargs.get('party')
        existingInvites = get_list_or_404(Invite, party_id=party)

class GuestsBrowseHostMode(generics.ListAPIView):
    serializer_class = UserSerializer
# Whether user is host is determined on frontend
    def get_queryset(self, *args, **kwargs):
        
        pk = self.kwargs.get('pk')
        parties = get_list_or_404(Party, host_id=pk)

        party = parties.pop()

        party_id = party.id
        # print(party_id)
        # party = self.kwargs.get('party')

        existingInvites = Invite.objects.filter(party_id_id=party_id).count()
        
        print(existingInvites)
        if existingInvites == 0:
            return User.objects.exclude(id=pk)
        
        else:
            existingGuests = []
            for v in Invite.objects.filter(party_id_id=party_id):
                # Appends the guest ids of all the invites to a list
                existingGuests.append(v.guest_id_id)
                if len(existingGuests) == len(Invite.objects.filter(party_id_id=party_id)):
                    # User.objects.filter()
                    return User.objects.exclude(id=pk).exclude(id__in=existingGuests)
            
            

            # print(existingGuests)
        # guest = existingInvites[0].guest_id_id
        # print(guest)

        # print(User.objects.get(id=pk).role)

        # role = User.objects.get(id=pk).role

            # parties = Party.objects.filter(host_id=pk)
            # myParty = parties.order_by('created_at').last()
            
            # existingInvites = get_list_or_404(Invite, party_id=myParty.id)

            # print(existingInvites)
            # existingGuestsIds = []
            # for i in existingInvites:
            #     existingGuestsIds.append(existingInvites[i])
            #     print(i)
            # 1. Find Most Recent Party
            # 2. Find all invites with the party id 
            # 3. Find all the guest_ids on those invites
            # 4. None of the objects gotten can contain ids same as any of those guest_ids
                
                # return User.objects.exclude(id in existingGuestsIds or pk)
            # Should not display user's own profile or any profiles associated with invited to their parties
            # This should only display bob right now
        
# # If user is not a host, Get all users that are not the user themselves
      
# # If user state is set to 'host', ensure that the guests are not associated with a invite already to the party

# # If user state is set to 'guest', prompt user to create a party


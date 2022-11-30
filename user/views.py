from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import UserSerializer
from .serializers import UserLoginSerializer
from .serializers import UserProfileSerializer, UserRoleSerializer
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

# Retrieve User model
User = get_user_model()
# Default user model from Django Admin

# Class based views for User Authentication

class RegisterView(generics.CreateAPIView):
    # Signup Page
    serializer_class = UserSerializer
    # permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
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

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView, mixins.UpdateModelMixin):
    # authentication_classes = [JWTAuthentication]
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    # permission_classes = (permissions.IsAdminUser | IsAuthorOrReadOnly,)
    # Comma says that this is a Tuple, but there is only one item -- Tuples are iterable and things in parentheses are not iterable -- If just parentheses without a comma: Then think you are just using then to tidy up code, does not know it is a Tuple
    def patch(request, *args, **kwargs):
        return User.objects.partial_update(request, *args, **kwargs)

class GuestsBrowse(generics.ListAPIView):
    serializer_class = UserSerializer
    def get_queryset(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        print(User.objects.get(id=pk).role)
        
        role = User.objects.get(id=pk).role
        if role == 0:
          return User.objects.exclude(id=pk)

#         if role == 1:
#             parties = Party.objects.filter(host_id=pk)
#             myParty = parties.order_by('created_at').last()
#             existingInvites = get_list_or_404(Invite, party_id=myParty.id)

#             existingGuestsIds = []
#             for i in existingInvites:
#                 existingGuestsIds.append(existingInvites[i].guest_id_id)
#             # 1. Find Most Recent Party
#             # 2. Find all invites with the party id 
#             # 3. Find all the guest_ids on those invites
#             # 4. None of the objects gotten can contain ids same as any of those guest_ids
#             return User.objects.get(id!=pk, id not in existingGuestsIds)
        
# # If user is not a host, Get all users that are not the user themselves
      
# # If user state is set to 'host', ensure that the guests are not associated with a invite already to the party

# # If user state is set to 'guest', prompt user to create a party


from rest_framework import serializers
from .models import Invite
from django.contrib.auth import get_user_model
from party.models import Party
from rest_framework import mixins

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "name", "department", "birthdate", "profile_picture")

class GuestSerializer(serializers.ModelSerializer):
    # Serializer for Guest Profile from Guestlist Page
    class Meta:
        model = get_user_model()
        fields = ("id", "name", "department", "birthdate", "profile_picture")

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ("id", "created_at", "host_id",
                  "flat", "first_entry", "vibe", )

# UNSURE: Where InviteSerializer is being used at the moment 
class InviteSerializer(serializers.ModelSerializer, mixins.CreateModelMixin):
    class Meta:
        model = Invite
        fields = ("id", "created_at", "updated_at", "party_id", "guest_id", "status", "plus_ones")
    
    # Get the party_id by searching through all parties with first_entry no more than 12 hours after .now()
    def create(self, validated_data):
        party_data = validated_data.pop("party_id")
        (party_id, _) = get_user_model().objects.get(**party_data)

        invite = Invite.objects.create(**validated_data, party_id=party_id)
        return invite

class CreateInviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = ("party_id", "guest_id")
    # To use send invite POST request 
    # 1. Get party belonging to host with PartyView
    # 2. Use party retrieved in body of request as a field 
    # 3. Use guest id as URL parameter to pass into CreateInviteView
    
    # def create(self, validated_data):
    #     my_view = self.context['view']
    #     object_id = my_view.kwargs.get('pk')

    #     invite = Invite.objects.create(**validated_data, guest_id=object_id)
    #     return invite 

class UpdateInviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = ("status",)

from rest_framework import serializers
from .models import Invite
from django.contrib.auth import get_user_model
from party.models import Party
from rest_framework import mixins

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("name", "department", "birthdate", "profile_picture")

class PartySerializer(serializers.ModelSerializer):
    host_id = HostSerializer()

    class Meta:
        model = Party
        fields = ("id", "created_at", "host_id",
                  "flat", "first_entry", "vibe", )

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

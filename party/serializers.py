from rest_framework import serializers
from .models import Party
from django.contrib.auth import get_user_model
from user.serializers import UserProfileSerializer

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ("flat", "first_entry", "vibe")

class PartyIdSerializer(serializers.ModelSerializer):
    # Used for MyPartyView
    # Only grabs party id to be used to create invite
    class Meta:
        model = Party
        fields = ("id",)

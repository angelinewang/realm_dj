from rest_framework import serializers
from .models import Party
from django.contrib.auth import get_user_model
from user.serializers import UserProfileSerializer

class PartySerializer(serializers.ModelSerializer):

    class Meta:
        model = Party
        fields = ("flat", "first_entry", "vibe")

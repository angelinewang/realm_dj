from rest_framework import serializers
from .models import Party
from django.contrib.auth import get_user_model


# class HostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ("name", "birthdate", "department", "profile_picture")

class PartySerializer(serializers.ModelSerializer):

    class Meta:
        model = Party
        fields = ("id", "created_at", "flat", "first_entry", "vibe", )

    def create(self, request, **validated_data):
        party = Party.objects.create(**validated_data, host_id=get_user_model(id=user))
        return party

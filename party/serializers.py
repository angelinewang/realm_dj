from rest_framework import serializers
from .models import Party
from django.contrib.auth import get_user_model
from user.serializers import UserProfileSerializer

# class HostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ("name", "birthdate", "department", "profile_picture")

class PartySerializer(serializers.ModelSerializer):

    class Meta:
        model = Party
        fields = ("id", "created_at", "flat", "first_entry", "vibe")

    # def create(self, **validated_data):
    #     # print(self.context['request'].user.id)

    #     # host_id=self.context['request'].user.id
    #     party = Party.objects.create(**validated_data)
    #     return party

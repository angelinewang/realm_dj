from rest_framework import serializers
from .models import Invite
from django.contrib.auth import get_user_model
from party.models import Party

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("tag",)

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username",)

class InviteSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    comments = CommentSerializer(read_only=True)
    author = AuthorSerializer()

    # Takes Database Model and converts into JSON and takes JSON and converts into a DB Model
    class Meta:
        model = Post
        fields = ("id", "author", "title", "body", "tags",
                  "comments", "created_at", "updated_at")

    def create(self, validated_data):
        author_data = validated_data.pop("author")
        (author, _) = get_user_model().objects.get_or_create(**author_data)

        tags_data = validated_data.pop("tags")

        for tag in tags_data:
            (tags, _) = Tag.objects.get_or_create(**tag)

        post = Post.objects.create(**validated_data, author=author, tags=tags)
        return post

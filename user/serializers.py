from rest_framework import serializers
from django.contrib.auth import get_user_model
import django.contrib.auth.password_validation as validations
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from party.models import Party

from rest_framework import permissions

User = get_user_model()

class FirstEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ("first_entry")

class UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError(
                {'password_confirmation': 'Passwords do not match!'})

        # This will check for a complex/secure password
        # try:
        #     validations.validate_password(password=password)
        # except ValidationError as err:
        #     raise serializers.ValidationError({'password': err.messages})

        data['password'] = make_password(password)
        return data

    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirmation')


class UserSerializer(serializers.ModelSerializer):
    permission_classes = [permissions.AllowAny]
    password = serializers.CharField(write_only=True)
    # password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
        password = data.pop('password')
        # password_confirmation = data.pop('password_confirmation')

        # if password != password_confirmation:
        #     raise serializers.ValidationError(
        #         {'password_confirmation': 'Passwords do not match!'})

        # This will check for a complex/secure password
        # try:
        #     validations.validate_password(password=password)
        # except ValidationError as err:
        #     raise serializers.ValidationError({'password': err.messages})

        # Creates a Hash from the string Password entered by user and stores the password as a Hash
        data['password'] = make_password(password)
        return data

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'name',
                  'birthdate', 'department', 'profile_picture', 'gender', 'profile_picture_data', 'file_image')

class UserProfileSerializer(serializers.ModelSerializer):
    # Used to fetch User Role, Host Profile, and User Profile Page
    class Meta:
        model = User
        fields = ('name', 'birthdate', 'department', 'profile_picture', 'gender', 'role')

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('role',)


class UpdatePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('profile_photo',)

# class Base64ImageField(serializers.ImageField):
#     """
#     A Django REST framework field for handling image-uploads through raw post data.
#     It uses base64 for encoding and decoding the contents of the file.

#     Heavily based on
#     https://github.com/tomchristie/django-rest-framework/pull/1268

#     Updated for Django REST framework 3.
#     """

#     def to_internal_value(self, data):
#         from django.core.files.base import ContentFile
#         import base64
#         import six
#         import uuid

#         # Check if this is a base64 string
#         if isinstance(data, six.string_types):
#             # Check if the base64 string is in the "data:" format
#             if 'data:' in data and ';base64,' in data:
#                 # Break out the header from the base64 content
#                 header, data = data.split(';base64,')

#             # Try to decode the file. Return validation error if it fails.
#             try:
#                 decoded_file = base64.b64decode(data)
#             except TypeError:
#                 self.fail('invalid_image')

#             # Generate file name:
#             # 12 characters are more than enough.
#             file_name = str(uuid.uuid4())[:12]
#             # Get the file name extension:
#             file_extension = self.get_file_extension(file_name, decoded_file)

#             complete_file_name = "%s.%s" % (file_name, file_extension, )

#             data = ContentFile(decoded_file, name=complete_file_name)

#         return super(Base64ImageField, self).to_internal_value(data)

#     def get_file_extension(self, file_name, decoded_file):
#         import imghdr


class UserSignUpSerializer(serializers.ModelSerializer):
    permission_classes = [permissions.AllowAny]
    password = serializers.CharField(write_only=True)
    # password_confirmation = serializers.CharField(write_only=True)
    # profile_picture = Base64ImageField(max_length=None, use_url=True)
    # print(profile_picture)

    def validate(self, data):
        password = data.pop('password')
        # password_confirmation = data.pop('password_confirmation')

        # if password != password_confirmation:
        #     raise serializers.ValidationError(
        #         {'password_confirmation': 'Passwords do not match!'})

        # This will check for a complex/secure password
        # try:
        #     validations.validate_password(password=password)
        # except ValidationError as err:
        #     raise serializers.ValidationError({'password': err.messages})

        # Creates a Hash from the string Password entered by user and stores the password as a Hash
        data['password'] = make_password(password)
        return data

    class Meta:
        model = User
        fields = ('profile_picture', 'email', 'password', 'name',
                  'birthdate', 'department', 'gender', 'profile_picture_data', 'file_image')

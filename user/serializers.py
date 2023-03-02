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
                  'department', 'profile_picture', 'gender', 'birthdate', 'birthday')

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

class UserSignUpSerializer(serializers.ModelSerializer):
    permission_classes = [permissions.AllowAny]
    password = serializers.CharField(write_only=True)
    # password_confirmation = serializers.CharField(write_only=True)
    # profile_picture = Base64ImageField(max_length=None, use_url=True)
    # print(profile_picture)

    def validate(self, data):
        password = data.pop('password')
        # print(data.get('birthdate'))
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
        fields = ('profile_picture', 'email', 'password', 'name', 'department', 'gender',
                  'birthdate', 'birthday')

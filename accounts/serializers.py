from rest_framework import serializers
from .models import MyUser
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate, login


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username','user_id','is_manager']

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model  = MyUser
        fields = ['username','password']
        extra_kwargs = {'password': {'write_only': True},}

    def create(self, validated_data):
        user = MyUser(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    class Meta:
        model = MyUser
        fields = ['username', 'password','user_id']
    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        return {'username': user.username}
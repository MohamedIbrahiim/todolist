from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    email = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        # These fields are only editable (not displayed) and have to be a part of 'fields' tuple
        extra_kwargs = {"password": {"write_only": True, "min_length": 8}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data.get("password"))
        user.save()
        return user

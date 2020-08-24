from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    role = serializers.IntegerField(required=True)
    SSN = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'first_name', 'last_name', 'role', 'SSN')
        extra_kwargs = {'password': {'write_only': True}, 'SSN': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    # def get_token(self, object):
    #     jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    #     jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    #     payload = jwt_payload_handler(object)
    #     token = jwt_encode_handler(payload)
    #     return token
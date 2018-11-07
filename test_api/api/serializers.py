from rest_framework import serializers
from ..models import TestApiModel
from django.contrib.auth import get_user_model

User = get_user_model()


class TestApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestApiModel
        fields = '__all__'
        read_only_fields = ('id', 'post_by')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        read_only_fields = ('username',)

    def validate_email(self, email):

        check_email = User.objects.filter(email__exact=email).exists()

        if check_email:
            raise serializers.ValidationError("The following email is already associated with another account.")
        return email


class CustomUserUpdateSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=22,
        read_only=True
    )
    email = serializers.EmailField(
        required=False,
        read_only=True
    )
    first_name = serializers.CharField(
        max_length=22,
        required=False
    )
    last_name = serializers.CharField(
        max_length=42,
        required=False
    )

    def validate_email(self, email):

        check_email = User.objects.filter(email__exact=email).exists()

        if check_email:
            raise serializers.ValidationError("The following email is already associated with another account.")
        return email

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance

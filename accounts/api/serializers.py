from rest_framework import serializers, exceptions, status
from owners.api.serializers import OwnerModelSerializer
from owners.models import OwnerModel
from django.contrib.auth.models import User
from django.db.models import Q


class UserModelWithOwnerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=50, write_only=True)
    password2 = serializers.CharField(min_length=8, max_length=50, write_only=True)
    owner = OwnerModelSerializer(many=False, read_only=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'owner')

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise exceptions.ValidationError(detail='Password must match.', code=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(Q(username=attrs.get('username')) | Q(email=attrs.get('email'))).exists():
            raise exceptions.ValidationError(
                detail='A user is already exists with that.',
                code=status.HTTP_400_BAD_REQUEST)
        return attrs

    def create(self, validated_data):
        owner_data = validated_data.pop('owner')
        obj = User.objects.create_user(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            password=validated_data.get('password')
        )
        OwnerModel.objects.create(
            owner_name=obj,
            **owner_data
        )
        return obj

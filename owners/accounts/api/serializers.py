from rest_framework import serializers, status
from owners.api.serializers import OwnerModelSerializer
from owners.models import OwnerModel
from django.contrib.auth.models import User
from django.db.models import Q
from userLevel.models import UserLevelModel


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
            raise serializers.ValidationError(detail='Passwords must match.', code=status.HTTP_400_BAD_REQUEST)
        return attrs

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                detail='A user is already exists with that email address.', code=status.HTTP_400_BAD_REQUEST)
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                detail='A user is already exists with that username.', code=status.HTTP_400_BAD_REQUEST)
        return value

    def request_data(self):
        return self.context['request']

    def request_user_data(self):
        return self.request_data().user

    def create(self, validated_data):
        if self.request_user_data().is_superuser is True:
            owner_data = validated_data.pop('owner')
            obj = User.objects.create_user(
                username=validated_data.get('username'),
                email=validated_data.get('email'),
                password=validated_data.get('password')
            )
            OwnerModel.objects.create(owner_name=obj, **owner_data)
            UserLevelModel.objects.create(user=obj, level=1)
            return obj
        raise serializers.ValidationError(
            detail="Your credentials are invalid to do this action. Are you a supersuer?",
            status=status.HTTP_400_BAD_REQUEST
            )

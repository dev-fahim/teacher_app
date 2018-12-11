from stores.api.serializers import OwnerStoreModelSerializer
from rest_framework import serializers
from owners.models import OwnerModel
from django.contrib.auth.models import User


class OwnerModelSerializer(serializers.ModelSerializer):
    owner_name = serializers.SerializerMethodField()
    store = OwnerStoreModelSerializer(many=True, read_only=True)

    class Meta:
        model = OwnerModel
        fields = '__all__'
        read_only_fields = (
            'id', 'owner_name', 'owner_joined'
        )

    @staticmethod
    def get_owner_name(obj):
        return str(obj.owner_name)


class CoreUserSerializer(serializers.ModelSerializer):
    owner = OwnerModelSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'owner'
        )
        read_only_fields = ('username', 'owner')

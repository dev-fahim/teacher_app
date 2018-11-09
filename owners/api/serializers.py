from rest_framework import serializers
from ..models import (OwnerModel, OwnerStoreModel)
from django.contrib.auth import get_user_model

User = get_user_model()


class OwnerStoreModelSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    urls = serializers.HyperlinkedIdentityField(view_name='api_owner:store_detail_api_view', lookup_field='id')

    class Meta:
        model = OwnerStoreModel
        fields = (
            'id', 'urls',
            'owner', 'owner_store_address',
            'owner_store_name',
            'owner_store_type', 'owner_store_added',
            'owner_store_updated', 'owner_store_lcs_type'
        )

    @staticmethod
    def get_owner(obj):
        return obj.get_owner_name


class OwnerModelSerializer(serializers.ModelSerializer):
    owner_name = serializers.SerializerMethodField()
    store = OwnerStoreModelSerializer(many=True, read_only=True)

    class Meta:
        model = OwnerModel
        fields = (
            'id', 'owner_name', 'owner_birth_date',
            'owner_ps_address', 'owner_pm_address',
            'owner_joined', 'store'
        )
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



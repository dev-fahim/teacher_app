from rest_framework import serializers
from ..models import (OwnerModel, OwnerStoreModel)
from django.contrib.auth import get_user_model

User = get_user_model()


class OwnerModelSerializer(serializers.ModelSerializer):
    owner_name = serializers.SerializerMethodField()

    class Meta:
        model = OwnerModel
        exclude = ('id',
                   'owner_is_active', 'owner_profile_submitted',
                   'owner_is_approved', 'owner_is_online'
                   )
        read_only_fields = ('owner_name', )

    @staticmethod
    def get_owner_name(obj):
        return str(obj.owner_name)


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

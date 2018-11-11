from ..owner_store_model_serializers.serializers import OwnerStoreModelSerializer
from rest_framework import serializers
from ....models import OwnerModel


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

from ..store_product_model_serializers.serializers import OwnerStoreProductModelSerializer
from rest_framework import serializers
from ....models import OwnerStoreModel


class OwnerStoreModelSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    urls = serializers.HyperlinkedIdentityField(
        view_name='api_owner:store_detail_api_view',
        lookup_field='id',
        read_only=True
    )
    products = OwnerStoreProductModelSerializer(many=True, read_only=True)

    class Meta:
        model = OwnerStoreModel
        fields = '__all__'
        read_only_fields = ('owner', )

    @staticmethod
    def get_owner(obj):
        return obj.get_owner_name

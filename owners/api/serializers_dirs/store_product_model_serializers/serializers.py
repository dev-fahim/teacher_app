from ..product_status_model_serializers.serializers import ProductStatusModelSerializer
from rest_framework import serializers
from ....models import StoreProductModel


class StoreProductModelSerializer(serializers.ModelSerializer):
    store_name = serializers.SerializerMethodField()
    urls = serializers.HyperlinkedIdentityField(
        view_name='api_owner:product_detail_api_view',
        lookup_field='id',
        read_only=True
    )

    class Meta:
        model = StoreProductModel
        fields = '__all__'
        read_only_fields = ('product_store', 'product_owner')

    @staticmethod
    def get_store_name(obj):
        return str(obj.get_store_name)


class OwnerStoreProductModelSerializer(serializers.ModelSerializer):
    store_name = serializers.SerializerMethodField()
    urls = serializers.HyperlinkedIdentityField(
        view_name='api_owner:product_status_detail_api_view',
        lookup_field='id',
        read_only=True
    )

    class Meta:
        model = StoreProductModel
        fields = '__all__'
        read_only_fields = ('product_store', 'product_owner')

    @staticmethod
    def get_store_name(obj):
        return str(obj.get_store_name)

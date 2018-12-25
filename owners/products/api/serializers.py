from rest_framework import serializers
from owners.products.models import (
    ProductStatusModel,
    StoreProductModel
)


class ProductStatusModelSerializer(serializers.ModelSerializer):
    urls = serializers.HyperlinkedIdentityField(
        view_name='api_product:product_detail_api_view',
        lookup_field='product_id',
        read_only=True
    )

    class Meta:
        model = ProductStatusModel
        fields = '__all__'
        read_only_fields = ('object_owner', 'product_origin')


class StoreProductModelSerializer(serializers.ModelSerializer):
    store_name = serializers.SerializerMethodField()
    urls = serializers.HyperlinkedIdentityField(
        view_name='api_product:product_detail_api_view',
        lookup_field='product_id',
        read_only=True
    )
    object_owner = serializers.SerializerMethodField()

    class Meta:
        model = StoreProductModel
        fields = '__all__'
        read_only_fields = ('product_store', 'product_owner', 'product_id')

    @staticmethod
    def get_store_name(obj):
        return str(obj.get_store_name)

    @staticmethod
    def get_object_owner(obj):
        return str(obj.get_owner_name)


class OwnerStoreProductModelSerializer(serializers.ModelSerializer):
    store_name = serializers.SerializerMethodField()
    urls = serializers.HyperlinkedIdentityField(
        view_name='api_product:product_status_detail_api_view',
        lookup_field='product_id',
        read_only=True
    )
    object_owner = serializers.SerializerMethodField()

    class Meta:
        model = StoreProductModel
        fields = '__all__'
        read_only_fields = ('product_store', 'object_owner', 'product_id')

    @staticmethod
    def get_store_name(obj):
        return str(obj.get_store_name)

    @staticmethod
    def get_object_owner(obj):
        return str(obj.get_owner_name)

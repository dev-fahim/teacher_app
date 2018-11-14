from rest_framework import serializers
from ....models import ProductStatusModel


class ProductStatusModelSerializer(serializers.ModelSerializer):
    urls = serializers.HyperlinkedIdentityField(
        view_name='api_owner:product_detail_api_view',
        lookup_field='product_id',
        read_only=True
    )

    class Meta:
        model = ProductStatusModel
        fields = '__all__'
        read_only_fields = ('object_owner', 'product_origin')


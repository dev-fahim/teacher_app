from rest_framework import generics, filters
from django.shortcuts import get_object_or_404
from products.api.serializers import (
    StoreProductModelSerializer,
    OwnerStoreProductModelSerializer,
    ProductStatusModelSerializer
)
from products.models import (
    StoreProductModel,
    ProductStatusModel
)
from products.api.utils import get_random_int_id


class StoreProductCreateAPIView(generics.ListCreateAPIView):
    serializer_class = StoreProductModelSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('product_name', 'product_id')

    def get_object(self):
        return self.request.user.owner

    def get_queryset(self):
        obj = self.get_object().store
        list_value = self.kwargs['list']
        obj = get_object_or_404(obj, id=list_value)
        return StoreProductModel.objects.filter(product_store=obj)

    def perform_create(self, serializer):
        product_id = get_random_int_id()
        obj = self.get_object().store
        list_value = self.kwargs['list']
        obj = get_object_or_404(obj, id=list_value)
        obj = serializer.save(product_store=obj, object_owner=self.get_object(), product_id=product_id)
        ProductStatusModel.objects.filter(product_origin=obj).update(
            object_owner=self.get_object(),
            product_id=product_id
        )


class StoreProductUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OwnerStoreProductModelSerializer
    lookup_field = 'product_id'

    def get_queryset(self):
        return StoreProductModel.objects.filter(object_owner=self.request.user.owner)


class StoreProductStatusUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductStatusModelSerializer
    lookup_field = 'product_id'

    def get_queryset(self):
        return ProductStatusModel.objects.filter(object_owner=self.request.user.owner)

    def perform_update(self, serializer):
        serializer.save(object_owner=self.request.user.owner)

from rest_framework import generics, filters
from django.shortcuts import get_object_or_404
from owners.products.api.serializers import (
    StoreProductModelSerializer,
    OwnerStoreProductModelSerializer,
    ProductStatusModelSerializer
)
from owners.products.models import (
    StoreProductModel,
    ProductStatusModel
)
from myproject.globals.api.permissions import IsOwnerOnly


class StoreProductCreateAPIView(generics.ListCreateAPIView):
    serializer_class = StoreProductModelSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('product_name', 'product_id')
    permission_classes = [IsOwnerOnly, ]

    def get_object(self):
        return self.request.user.owner

    def get_queryset(self):
        obj = self.get_object().store
        list_value = self.kwargs['list']
        obj = get_object_or_404(obj, id=list_value)
        return StoreProductModel.objects.filter(product_store=obj)

    def perform_create(self, serializer):
        obj = self.get_object().store
        list_value = self.kwargs['list']
        obj = get_object_or_404(obj, id=list_value)
        serializer.save(product_store=obj, object_owner=self.get_object())


class StoreProductUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOnly, ]
    serializer_class = OwnerStoreProductModelSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return StoreProductModel.objects.filter(object_owner=self.request.user.owner)


class StoreProductStatusUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOnly, ]
    serializer_class = ProductStatusModelSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return ProductStatusModel.objects.filter(object_owner=self.request.user.owner)

    def perform_update(self, serializer):
        serializer.save(object_owner=self.request.user.owner)

from rest_framework import generics, views, response
from rest_framework import permissions
from .serializers import *
from django.shortcuts import get_list_or_404, get_object_or_404
from ..models import *


class AllInformationListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return self.get_object()

    def get_object(self):
        return self.request.user

    def get_serializer(self, *args, **kwargs):
        return CoreUserSerializer(self.get_queryset(), context={'request': self.request})


class OwnerAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get_object(self):
        return self.request.user.owner

    def get_serializer(self, *args, **kwargs):
        return OwnerModelSerializer(instance=self.get_object(), context={'request': self.request})


class OwnerStoreAPIView(generics.ListCreateAPIView):
    serializer_class = OwnerStoreModelSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return self.get_object()

    def get_object(self):
        return self.request.user.owner.store

    def perform_create(self, serializer):
        return serializer.save(owner_store=self.request.user.owner)


class OwnerStoreDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = OwnerStoreModelSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return self.request.user.owner.store


class StoreProductCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = StoreProductModelSerializer

    def get_object(self):
        return self.request.user.owner

    def get_queryset(self, *args, **kwargs):
        obj = self.get_object().store
        obj = get_object_or_404(obj, id=self.request.GET.get('list'))
        return StoreProductModel.objects.filter(product_store=obj)

    def perform_create(self, serializer):
        obj = self.get_object().store
        obj = get_object_or_404(obj, id=self.request.GET.get('list'))
        obj = serializer.save(product_store=obj, store_product_owner=self.request.user.owner)
        ProductStatusModel.objects.filter(product_origin=obj).update(product_owner=self.request.user.owner)


class StoreProductUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = OwnerStoreProductModelSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return StoreProductModel.objects.filter(store_product_owner=self.request.user.owner)


class StoreProductStatusUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ProductStatusModelSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return ProductStatusModel.objects.filter(product_owner=self.request.user.owner)

    def perform_update(self, serializer):
        serializer.save(product_owner=self.request.user.owner)


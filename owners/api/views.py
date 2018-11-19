from rest_framework import generics
from rest_framework import permissions
from rest_framework import exceptions
from .serializers import *
from django.shortcuts import get_object_or_404
from ..models import *
from .utils import get_random_int_id


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
        list_value = self.request.query_params.get('list', None)
        if list_value is not None and isinstance(list_value, str) and list_value.isdigit():
            obj = get_object_or_404(obj, id=list_value)
            return StoreProductModel.objects.filter(product_store=obj)
        else:
            raise exceptions.ValidationError("You ..ck", "Not allowed.")  # we have set a viewable validation error here

    def perform_create(self, serializer):
        product_id = get_random_int_id()
        obj = self.get_object().store
        list_value = self.request.query_params.get('list', None)
        if list_value is not None and isinstance(list_value, str) and list_value.isdigit():
            obj = get_object_or_404(obj, id=list_value)
            obj = serializer.save(product_store=obj, object_owner=self.get_object(), product_id=product_id)
            ProductStatusModel.objects.filter(product_origin=obj).update(
                object_owner=self.get_object(),
                product_id=product_id
            )
        else:
            raise exceptions.ValidationError("You ..ck", "Not allowed.")  # we have set a viewable validation error here


class StoreProductUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = OwnerStoreProductModelSerializer
    lookup_field = 'product_id'

    def get_queryset(self):
        return StoreProductModel.objects.filter(object_owner=self.request.user.owner)


class StoreProductStatusUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ProductStatusModelSerializer
    lookup_field = 'product_id'

    def get_queryset(self):
        return ProductStatusModel.objects.filter(object_owner=self.request.user.owner)

    def perform_update(self, serializer):
        serializer.save(object_owner=self.request.user.owner)


class ReadOnlyTestAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    serializer_class = OwnerStoreModelSerializer
    queryset = OwnerStoreModel.objects.all()


class ReadOnlyDetailTestAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    serializer_class = OwnerStoreModelSerializer
    queryset = OwnerStoreModel.objects.all()
    lookup_field = 'id'


class ReadOnlyDetailProductTestAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    serializer_class = OwnerStoreProductModelSerializer
    queryset = StoreProductModel.objects.all()

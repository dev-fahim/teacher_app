from rest_framework import generics
from owners.stores.api.serializers import (OwnerStoreModelSerializer)
from myproject.globals.api.permissions import IsOwnerOnly


class OwnerStoreAPIView(generics.ListCreateAPIView):
    serializer_class = OwnerStoreModelSerializer
    permission_classes = [IsOwnerOnly, ]

    def get_queryset(self):
        return self.get_object()

    def get_object(self):
        return self.request.user.owner.store

    def perform_create(self, serializer):
        return serializer.save(object_owner=self.request.user.owner)


class OwnerStoreDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OwnerStoreModelSerializer
    permission_classes = [IsOwnerOnly, ]
    lookup_field = 'id'

    def get_queryset(self):
        return self.request.user.owner.store

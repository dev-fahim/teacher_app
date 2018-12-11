from rest_framework import generics
from stores.api.serializers import (OwnerStoreModelSerializer)


class OwnerStoreAPIView(generics.ListCreateAPIView):
    serializer_class = OwnerStoreModelSerializer

    def get_queryset(self):
        return self.get_object()

    def get_object(self):
        return self.request.user.owner.store

    def perform_create(self, serializer):
        return serializer.save(object_owner=self.request.user.owner)


class OwnerStoreDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OwnerStoreModelSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return self.request.user.owner.store

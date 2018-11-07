from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwner
from ..models import (OwnerModel, OwnerStoreModel)
from . serializers import (OwnerModelSerializer, OwnerStoreModelSerializer)


class OwnerListAPIView(generics.ListCreateAPIView):
    serializer_class = OwnerModelSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def perform_create(self, serializer):
        return serializer.save(owner_name=self.request.user)

    def get_queryset(self):
        return OwnerModel.objects.filter(owner_name__exact=self.request.user)


class OwnerStoreListAPIView(generics.ListCreateAPIView):
    serializer_class = OwnerStoreModelSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return OwnerStoreModel.objects.filter(owner_store=self.request.user.owner)

    def perform_create(self, serializer):
        return serializer.save(owner_store=self.request.user.owner)

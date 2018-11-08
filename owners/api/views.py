from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .serializers import *


class AllInformationListView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get_object(self):
        return self.request.user.owner

    def get_queryset(self):
        return self.get_object()

    def get(self, request, *args, **kwargs):
        owner = self.get_queryset()
        stores = self.get_queryset().store
        owner_serializer = OwnerModelSerializer(owner)
        stores_serializer = OwnerStoreModelSerializer(stores, many=True, context={'request': request})
        stores = stores_serializer.data
        if len(stores) is 0:
            stores = 'No stores are associated with you.'
        content = [
            {
                'owner': {
                    'info': owner_serializer.data,
                    'stores': stores
                }
            }
        ]
        return Response(data=content)


class OwnerAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = OwnerModelSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_object(self):
        return self.request.user.owner


class OwnerStoreAPIView(generics.ListCreateAPIView):
    serializer_class = OwnerStoreModelSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return self.get_object()

    def get_object(self):
        return self.request.user.owner.store

    def perform_create(self, serializer):
        return serializer.save(owner_store=self.request.user.owner)


class OwnerStoreDetailAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = OwnerStoreModelSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    lookup_field = 'id'

    def get_queryset(self):
        return self.request.user.owner.store




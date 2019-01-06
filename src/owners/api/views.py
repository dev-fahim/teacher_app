from rest_framework import generics
from rest_framework import permissions
from owners.api.serializers import (
    OwnerModelSerializer,
    CoreUserSerializer
)
from myproject import userLevePermission


class AllInformationListView(generics.ListAPIView):
    permission_classes = [userLevePermission.IsOwner, ]

    def get_queryset(self):
        return self.get_object()

    def get_object(self):
        return self.request.user

    def get_serializer(self, *args, **kwargs):
        return CoreUserSerializer(self.get_queryset(), context={'request': self.request})


class OwnerAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [userLevePermission.IsOwner, ]
    serializer_class = OwnerModelSerializer

    def get_object(self):
        return self.request.user.owner

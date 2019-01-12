from owners.accounts.api.serializers import UserModelWithOwnerSerializer
from rest_framework import generics
from myproject.globals.api.permissions import IsOwnerOnly


class RegisterOwner(generics.CreateAPIView):
    serializer_class = UserModelWithOwnerSerializer
    permission_classes = [
        IsOwnerOnly
    ]

    def get_queryset(self):
        return self.request.user.owner

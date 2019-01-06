from owners.accounts.api.serializers import UserModelWithOwnerSerializer
from rest_framework import generics
from myproject import userLevePermission


class RegisterOwner(generics.CreateAPIView):
    serializer_class = UserModelWithOwnerSerializer
    permission_classes = [
        userLevePermission.IsOwner
    ]

    def get_queryset(self):
        return self.request.user.owner

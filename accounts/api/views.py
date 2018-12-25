from accounts.api.serializers import UserModelWithOwnerSerializer
from rest_framework import generics


class RegisterOwner(generics.CreateAPIView):
    serializer_class = UserModelWithOwnerSerializer

    def get_queryset(self):
        return self.request.user.owner

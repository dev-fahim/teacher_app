from rest_framework import generics
from rest_framework.response import Response
from cashiers.api.serializers import CashierUserModelSerializer, CashierModelSerializer
from myproject import userLevePermission


class CashierAPIView(generics.GenericAPIView):
    permission_classes = [
        userLevePermission.IsOwner,
    ]

    @staticmethod
    def get(request):
        serializer = CashierUserModelSerializer(instance=request.user)
        return Response(serializer.data)


class CashierCreateAPIView(generics.CreateAPIView):
    serializer_class = CashierUserModelSerializer
    permission_classes = [
        userLevePermission.IsOwner,
    ]

    def get_queryset(self):
        return self.request.user


class CashierListApiView(generics.ListAPIView):
    serializer_class = CashierModelSerializer
    permission_classes = [
        userLevePermission.IsOwner,
    ]

    def get_queryset(self):
        return self.request.user.owner.cashier_owner

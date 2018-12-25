from rest_framework import views, generics
from rest_framework.response import Response
from cashiers.api.serializers import CashierUserModelSerializer


class CashierListCreateAPIView(generics.GenericAPIView):
    @staticmethod
    def get(request):
        serializer = CashierUserModelSerializer(instance=request.user)
        return Response(serializer.data)


class CashierCreateAPIView(generics.CreateAPIView):
    serializer_class = CashierUserModelSerializer

    def get_queryset(self):
        return self.request.user

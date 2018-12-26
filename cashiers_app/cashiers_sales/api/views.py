from cashiers_app.cashiers_sales.api.serializers import CashierSaleMainSerializer
from rest_framework import generics


class SalesListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CashierSaleMainSerializer

    def get_queryset(self):
        return self.request.user.cashier

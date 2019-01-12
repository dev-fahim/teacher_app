from rest_framework import generics
from sales.api.serializers import SalesSerializer
from sales.models import SalesModel
from django.shortcuts import get_object_or_404
from rest_framework import filters
from myproject import userLevePermission
from sales.api.permissons import IsOwnerOrCashierForSales


class SalesListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = SalesSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('sales_object__product__product_name', 'sales_object__product__product_id', 'sale_id')
    permission_classes = [IsOwnerOrCashierForSales, ]

    def get_object(self):
        return self.request.user.owner

    def get_queryset(self):
        return self.get_object().sales_owner


class SalesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrCashierForSales, ]
    serializer_class = SalesSerializer
    lookup_field = 'id'
    """
    def get_queryset(self):
        return self.request.user.owner.sales_owner
    """


"""
class SalesRetrieveUpdateDestroyAPIView(generics.RetrieveAPIView):
    permission_classes = [userLevePermission.IsOwner]
    serializer_class = SalesSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return self.request.user.owner.sales_owner

"""


class SalesStoreWiseListAPIView(generics.ListAPIView):
    permission_classes = [IsOwnerOrCashierForSales, ]
    serializer_class = SalesSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('sales_object__product__product_name', 'sales_object__product__product_id', 'sale_id')

    def get_queryset(self):
        sid = self.kwargs['sid']
        store = get_object_or_404(self.request.user.owner.store, id=sid)
        return SalesModel.objects.filter(object_owner=self.request.user.owner, store=store)

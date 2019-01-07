from rest_framework.permissions import BasePermission
from owners.stores.models import OwnerStoreModel
from owners.models import OwnerModel
from cashiers.models import CashierModel


class IsOwnerOrCashierForSales(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if OwnerModel.objects.filter(owner_name=request.user):
            return OwnerStoreModel.objects.filter(object_owner=obj.object_owner, id=obj.store.id).exists()
        return CashierModel.objects.filter(cashier_user=request.user, cashier_store=obj.store).exists()

    def has_permission(self, request, view):
        return request.user.is_authenticated

from rest_framework.permissions import BasePermission
from owners.stores.models import OwnerStoreModel
from owners.models import OwnerModel
from owners.stores.models import OwnerStoreModel
from cashiers.models import CashierModel


class IsOwnerOrCashierForSales(BasePermission):

    def has_object_permission(self, request, obj, view):
        if request.user.is_authenticated:
            if CashierModel.objects.filter(cashier_user=request.user):
                return CashierModel.objects.filter(cashier_user=request.user, cashier_store=obj.store).exists()
            elif OwnerModel.objects.filter(owner_name=request.user):
                return OwnerStoreModel.objects.filter(object_owner=request.user, id=obj.store.id)
        return False

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if CashierModel.objects.filter(cashier_user=request.user) or OwnerModel.objects.filter(owner_name=request.user):
                return True
        return False

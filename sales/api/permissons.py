from rest_framework.permissions import BasePermission
from owners.stores.models import OwnerStoreModel


class IsOwnerOrCashier(BasePermission):
     
    def has_object_permission(self, request, obj):
        return OwnerStoreModel.objects.filter(object_owner=request.user)

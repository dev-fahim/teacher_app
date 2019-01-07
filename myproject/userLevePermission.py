from rest_framework import permissions
from django.contrib.auth.models import User
from cashiers.models import CashierModel
from owners.models import OwnerModel
from owners.stores.models import OwnerStoreModel
from userLevel.models import UserLevelModel


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        level = request.user.user_level.level
        if level >= 2:
            return OwnerModel.objects.filter(owner_name=request.user).exists()

    def has_permission(self, request, view):
        return request.user.is_authenticated


class IsCashier(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return CashierModel.objects.filter(cashier_user=request.user)

    def has_permission(self, request, view):
        return request.user.is_authenticated

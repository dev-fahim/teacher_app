from rest_framework import permissions
from owners.models import OwnerModel


class IsOwnerOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return OwnerModel.objects.filter(owner_name=request.user).exists()
        return False

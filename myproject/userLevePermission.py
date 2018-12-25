from rest_framework import permissions
from django.contrib.auth.models import User


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.method in permissions.SAFE_METHODS:
            if obj == request.user:
                return obj.owner == request.user.owner
            if obj == request.user.owner:
                return True
            return obj.object_owner == request.user.owner
        return False

    def has_permission(self, request, view):
        return request.user.is_authenticated


class IsCashier(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.method in permissions.SAFE_METHODS:
            return obj.object_cashier == request.user.cashier
        return False

    def has_permission(self, request, view):
        return request.user.is_authenticated

from rest_framework import permissions, filters
from owners.models import OwnerModel


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(OwnerModel.objects.filter(owner_name=request.user).exists())
        return OwnerModel.objects.filter(owner_name=request.user).exists()

    def has_permission(self, request, view):
        return OwnerModel.objects.filter(owner_name=request.user).exists()


class IsOwnerFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(object_owner=request.user.owner)

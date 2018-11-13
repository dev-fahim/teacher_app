from rest_framework import permissions, filters


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user and permissions.SAFE_METHODS:
                return True
        return obj.owner_store == request.user.owner

    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        return False


class IsOwnerFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(object_owner=request.user.owner)


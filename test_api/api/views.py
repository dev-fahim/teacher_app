from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, BasePermission, IsAuthenticated, SAFE_METHODS
from ..models import TestApiModel
from .serializers import TestApiSerializer, CustomUserUpdateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user and SAFE_METHODS:
            if obj.post_by == request.user:
                return True
            else:
                return False

    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        return False


class UserDetailsAPIView(RetrieveUpdateAPIView):
    serializer_class = CustomUserUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class TestAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TestApiSerializer

    def get_queryset(self):
        qs = TestApiModel.objects.filter(post_by__exact=self.request.user.pk)
        return qs

    def perform_create(self, serializer):
        return serializer.save(post_by=self.request.user)


class TestAPIUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner, IsAdminUser, IsAuthenticatedOrReadOnly]
    serializer_class = TestApiSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return TestApiModel.objects.all()

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        return obj

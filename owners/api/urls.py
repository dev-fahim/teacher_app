from django.urls import path
from .views import (OwnerListAPIView, OwnerStoreListAPIView)

urlpatterns = [
    path('apis/v1/owner/', OwnerListAPIView.as_view()),
    path('apis/v1/owner/stores', OwnerStoreListAPIView.as_view()),
]

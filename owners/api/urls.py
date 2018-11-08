from django.urls import path
from .views import (OwnerAPIView, OwnerStoreAPIView, AllInformationListView, OwnerStoreDetailAPIView)

app_name = 'api_owner'

urlpatterns = [
    path('apis/v1/owner/', OwnerAPIView.as_view()),
    path('apis/v1/owner/stores/', OwnerStoreAPIView.as_view()),
    path('apis/v1/owner/stores/<int:id>/', OwnerStoreDetailAPIView.as_view(), name='store_detail_api_view'),
    path('apis/v1/info/', AllInformationListView.as_view())
]

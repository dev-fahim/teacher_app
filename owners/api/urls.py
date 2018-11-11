from django.urls import path
from .views import *

app_name = 'api_owner'

urlpatterns = [
    path('apis/v2/owner/', OwnerAPIView.as_view()),
    path('apis/v2/owner/stores/', OwnerStoreAPIView.as_view()),
    path('apis/v2/owner/stores/<int:id>/', OwnerStoreDetailAPIView.as_view(), name='store_detail_api_view'),
    path('apis/v2/owner/info/', AllInformationListView.as_view()),
    path('apis/v2/owner/stores/products/', StoreProductCreateAPIView.as_view()),
    path('apis/v2/owner/stores/product/<int:id>/',
         StoreProductUpdateAPIView.as_view(),
         name="product_detail_api_view"),
    path('apis/v2/owner/stores/product/status/<int:id>/',
         StoreProductStatusUpdateAPIView.as_view(),
         name="product_status_detail_api_view"),
]

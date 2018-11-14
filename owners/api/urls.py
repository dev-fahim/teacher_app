from django.urls import path, include
from .views import *

app_name = 'api_owner'

urlpatterns = [
    path('apis/v2/', include([
        path('owner/', OwnerAPIView.as_view()),
        path('owner/stores/', OwnerStoreAPIView.as_view()),
        path('owner/stores/<int:id>/', OwnerStoreDetailAPIView.as_view(), name='store_detail_api_view'),
        path('owner/info/', AllInformationListView.as_view()),
        path('owner/stores/products/', StoreProductCreateAPIView.as_view()),
        path('owner/stores/product/<int:product_id>/',
             StoreProductUpdateAPIView.as_view(),
             name="product_detail_api_view"),
        path('owner/stores/product/status/<int:product_id>/',
             StoreProductStatusUpdateAPIView.as_view(),
             name="product_status_detail_api_view"),
        path('stores/', ReadOnlyTestAPIView.as_view()),
    ]))
]

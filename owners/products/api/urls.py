from django.urls import path, include
from owners.products.api.views import (
    StoreProductCreateAPIView,
    StoreProductUpdateAPIView,
    StoreProductStatusUpdateAPIView
)

app_name = 'api_product'

urlpatterns = [
    path('owner/store/', include([
        path('<int:list>/products/', StoreProductCreateAPIView.as_view()),
        path('product/<uuid:product_id>/',
             StoreProductUpdateAPIView.as_view(),
             name="product_detail_api_view"),
        path('product/status/<uuid:product_id>/',
             StoreProductStatusUpdateAPIView.as_view(),
             name="product_status_detail_api_view")
    ]))
]

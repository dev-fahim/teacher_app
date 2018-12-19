from django.urls import path, include
from products.api.views import (
    StoreProductCreateAPIView,
    StoreProductUpdateAPIView,
    StoreProductStatusUpdateAPIView
)

app_name = 'api_product'

urlpatterns = [
    path('apis/v2/owner/store/', include([
        path('products/<int:list>/', StoreProductCreateAPIView.as_view()),
        path('product/<int:product_id>/',
             StoreProductUpdateAPIView.as_view(),
             name="product_detail_api_view"),
        path('product/status/<int:product_id>/',
             StoreProductStatusUpdateAPIView.as_view(),
             name="product_status_detail_api_view")
    ]))
]

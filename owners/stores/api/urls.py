from django.urls import path, include
from owners.stores.api.views import (
    OwnerStoreAPIView,
    OwnerStoreDetailAPIView
)

app_name = 'api_store'

urlpatterns = [
    path('owner/', include([
        path('store/', OwnerStoreAPIView.as_view()),
        path('store/<int:id>/', OwnerStoreDetailAPIView.as_view(), name='store_detail_api_view')
    ]))
]

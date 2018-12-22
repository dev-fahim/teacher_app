from django.urls import path, include
from sales.api.views import (
    SalesListCreateAPIView,
    SalesRetrieveUpdateDestroyAPIView,
    SalesStoreWiseListAPIView
)

app_name = 'api_sales'

urlpatterns = [
    path('owner/dailysales/', include([
        path('', SalesListCreateAPIView.as_view()),
        path('<int:id>/', SalesRetrieveUpdateDestroyAPIView.as_view(), name='sales_detail_api_view'),
        path('store/<int:sid>/', SalesStoreWiseListAPIView.as_view())
    ])),
]

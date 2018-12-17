from django.urls import path, include
from sales.api.views import SalesListCreateAPIView, SalesRetrieveUpdateDestroyAPIView, sales_store_wise_list_api_view

app_name = 'api_sales'

urlpatterns = [
    path('apis/v2/owner/dailysales/', include([
        path('', SalesListCreateAPIView.as_view()),
        path('<int:id>/', SalesRetrieveUpdateDestroyAPIView.as_view(), name='sales_detail_api_view'),
        path('store/<int:sid>/', sales_store_wise_list_api_view)
    ])),
]

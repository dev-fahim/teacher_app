from django.urls import path, include
from cashiers_app.cashiers_sales.api.views import SalesListCreateAPIView

urlpatterns = [
    path('cashier/', include([
        path('dailysales/', SalesListCreateAPIView.as_view())
    ]))
]

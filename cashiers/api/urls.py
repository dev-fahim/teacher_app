from django.urls import path, include
from cashiers.api.views import CashierListCreateAPIView, CashierCreateAPIView

app_name = 'api_cashier'

urlpatterns = [
    path('cashier/', include([
        path('', CashierListCreateAPIView.as_view()),
        path('create/', CashierCreateAPIView.as_view()),
    ])),
]

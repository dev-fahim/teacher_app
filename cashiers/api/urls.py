from django.urls import path, include
from cashiers.api.views import CashierListCreateAPIView

app_name = 'api_cashier'

urlpatterns = [
    path('cashier/', include([
        path('all/', CashierListCreateAPIView.as_view()),
    ])),
]

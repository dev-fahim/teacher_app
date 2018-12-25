from django.urls import path, include
from owners.cashiers.api.views import CashierAPIView, CashierCreateAPIView, CashierListApiView

app_name = 'api_cashier'

urlpatterns = [
    path('cashier/', include([
        path('', CashierAPIView.as_view()),
        path('all/', CashierListApiView.as_view()),
        path('create/', CashierCreateAPIView.as_view()),
    ])),
]

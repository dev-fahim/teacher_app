from django.urls import path, include
from cashiers.api.views import CashierCreateAPIView, CashierListApiView

app_name = 'api_cashier'

urlpatterns = [
    path('owner/cashiers/', include([
        path('', CashierListApiView.as_view()),
        path('create/', CashierCreateAPIView.as_view()),
    ])),
]

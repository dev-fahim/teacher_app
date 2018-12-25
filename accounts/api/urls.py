from django.urls import path
from accounts.api.views import RegisterOwner

app_name = 'api_accounts'

urlpatterns = [
    path('register', RegisterOwner.as_view()),
]

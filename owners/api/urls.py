from django.urls import path, include
from .views import *

app_name = 'api_owner'

urlpatterns = [
    path('apis/v2/', include([
        path('owner/', OwnerAPIView.as_view()),
        path('owner/info/', AllInformationListView.as_view()),
    ]))
]

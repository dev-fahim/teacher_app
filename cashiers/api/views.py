from rest_framework import views
from rest_framework.response import Response
from cashiers.api.serializers import CashierUserModelSerializer


class CashierListCreateAPIView(views.APIView):


    def get(self, request):
        serializer = CashierUserModelSerializer(instance=request.user)
        return Response(serializer.data)



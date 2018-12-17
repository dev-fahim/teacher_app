from rest_framework import generics
from sales.api.serializers import SalesSerializer
from sales.models import SalesModel
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class SalesListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = SalesSerializer

    def get_object(self):
        return self.request.user.owner

    def get_queryset(self):
        return self.get_object().sales_owner


class SalesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SalesSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return self.request.user.owner.sales_owner


@api_view(['GET'])
def sales_store_wise_list_api_view(request, sid):

    if request.method == 'GET':
        store = get_object_or_404(request.user.owner.store, id=sid)
        obj = SalesModel.objects.filter(object_owner=request.user.owner, store=store)
        if obj.exists():
            serializer = SalesSerializer(instance=obj, many=True, context={'request': request})
            return Response(serializer.data)
        return Response(data={'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    return Response(data={'detail': 'Not acceptable'}, status=status.HTTP_403_FORBIDDEN)

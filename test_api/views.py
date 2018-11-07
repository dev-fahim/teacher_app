from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def objects_func_view(request):
    return Response([])


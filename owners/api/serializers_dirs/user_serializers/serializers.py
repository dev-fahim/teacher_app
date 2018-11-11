from ..owner_model_serializers.serializers import OwnerModelSerializer
from rest_framework import serializers
from ....models import User


class CoreUserSerializer(serializers.ModelSerializer):
    owner = OwnerModelSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'owner'
        )
        read_only_fields = ('username', 'owner')

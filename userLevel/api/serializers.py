from rest_framework import serializers
from userLevel.models import UserLevelModel


class UserLevelModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserLevelModel
        fields = '__all__'
        read_only_fields = ('user', 'level')

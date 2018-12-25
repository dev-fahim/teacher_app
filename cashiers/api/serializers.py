from rest_framework import serializers, status
from django.contrib.auth.models import User
from rest_framework import exceptions
from django.db.models import Q
from cashiers.models import CashierModel
from stores.models import OwnerStoreModel


class CashierModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CashierModel
        fields = '__all__'
        read_only_fields = ('object_owner', 'cashier_id', 'cashier_user')


class CashierUserModelSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=50, write_only=True)
    password2 = serializers.CharField(min_length=8, max_length=50, write_only=True)
    cashier = CashierModelSerializer(many=False, read_only=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'cashier')

    def validate(self, attrs):
        request = self.context['request']
        password = attrs.get('password')
        password2 = attrs.get('password2')
        cashier_data = attrs.get('cashier')

        if password != password2:
            raise exceptions.ValidationError(detail='Password must match.', code=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(Q(username=attrs.get('username')) | Q(email=attrs.get('email'))).exists():
            raise exceptions.ValidationError(detail='Already exists', code=status.HTTP_400_BAD_REQUEST)
        if OwnerStoreModel.objects.filter(object_owner=request.user.owner, owner_store_name=cashier_data.get('cashier_store')).exists() is False:
            raise exceptions.ValidationError(detail='Store not found', code=status.HTTP_400_BAD_REQUEST)
        return attrs

    def create(self, validated_data):
        request = self.context['request']
        user = request.user.owner
        cashier_all_data = validated_data.pop('cashier')
        obj = User.objects.create_user(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            password=validated_data.get('password')
        )
        CashierModel.objects.create(
            object_owner=user,
            cashier_user=obj,
            cashier_id='',
            **cashier_all_data
        )
        return obj

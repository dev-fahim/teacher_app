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
        read_only_fields = ('cashier_owner', 'cashier_id')


class CashierUserModelSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=50, write_only=True)
    password2 = serializers.CharField(min_length=8, max_length=50, write_only=True)
    cashier_user = CashierModelSerializer(many=False, read_only=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'cashier_user', 'password', 'password2')

    def validate(self, attrs):
        request = self.context['request']
        password = attrs.get('password')
        password2 = attrs.get('password2')
        cashier_data = attrs.pop('cashier_user')

        if password != password2:
            raise exceptions.ValidationError(detail='Password must match.', code=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(Q(username=attrs.get('username')) | Q(email=attrs.get('email'))).exists():
            raise exceptions.ValidationError(detail='Already exists', code=status.HTTP_400_BAD_REQUEST)
        if OwnerStoreModel.objects.filter(object_owner=request.user.owner, owner_store_name=cashier_data.get('cashier_store')).exists() is False:
            raise exceptions.ValidationError(detail='Store not found', code=status.HTTP_400_BAD_REQUEST)
        return attrs

    def create(self, validated_data):
        request = self.context['request']
        cashier_data = validated_data.pop('cashier_user')
        print(cashier_data)
        obj = User.objects.create_user(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            password=validated_data.get('password')
        )
        CashierModel.objects.create(
            object_owner=request.user.owner,
        )
        return obj

from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import exceptions
from django.db.models import Q
from cashiers.models import CashierModel


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
    cashier_model = CashierModelSerializer(many=False, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'cashier_model', 'password', 'password2')

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')

        if password != password2:
            raise exceptions.ValidationError(detail='Password must match.', code=400)
        if User.objects.filter(Q(username=attrs.get('username')) | Q(email=attrs.get('email'))).exists():
            raise exceptions.ValidationError(detail='Already exists.', code=400)

        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        cashier_model = validated_data.pop('cashier_model')
        if User.objects.filter(
                Q(username=validated_data.get('username')) | Q(email=validated_data.get('email'))
        ).exists():
            raise exceptions.ValidationError(detail='Already exists.', code=400)
        return User.objects.create_user(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            password=validated_data.get('password')
        )

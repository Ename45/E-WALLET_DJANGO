from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from wallet.models import Wallet
from wallet_user.models import User


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['email', 'phone_number', 'password', 'first_name', 'last_name', 'username']

    # def create(self, validated_data):
    #     user_id = User.pk
    #     phone_number = validated_data['phone_number']
    #     return Wallet.objects.create(user_id=user_id, wallet_number=phone_number[1:])

from rest_framework import serializers

from wallet.models import Wallet, Transaction
from wallet_user.serializer import CreateUserSerializer


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['wallet_number', 'balance', 'user']

        user = CreateUserSerializer()


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['transaction_type', 'transaction_status', 'date_added', 'amount', 'wallet']

        wallet = WalletSerializer()

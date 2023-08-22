from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from wallet.models import Wallet, Transaction
from wallet.serializer import WalletSerializer, TransactionSerializer


# Create your views here.
class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

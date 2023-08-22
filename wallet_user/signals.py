from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from wallet.models import Wallet
from wallet_user.models import User


@receiver(post_save, sender=User)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(
            user=instance, wallet_number=instance.phone_number[1:]
        )
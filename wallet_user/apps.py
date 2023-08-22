from django.apps import AppConfig


class WalletUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wallet_user'

    def ready(self) -> None:
        import wallet_user.signals

from django.apps import AppConfig


class EcommerceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ecommerce'

    # Wire the signal into the app
    def ready(self):
        import ecommerce.signals

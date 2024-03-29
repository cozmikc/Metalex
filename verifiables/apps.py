from django.apps import AppConfig


class VerifiablesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'verifiables'

    def ready(self):
        import verifiables.signals

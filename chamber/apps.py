from django.apps import AppConfig


class ChamberConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chamber'


    def ready(self):
        import chamber.signals
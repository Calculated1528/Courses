from django.apps import AppConfig
from django.db.models import signals

class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'

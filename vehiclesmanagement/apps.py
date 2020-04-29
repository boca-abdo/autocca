from django.apps import AppConfig


class VehiclesmanagementConfig(AppConfig):
    name = 'vehiclesmanagement'

    def ready(self):
        from .signals import *

from django.db.models.signals import post_save
from django.dispatch import receiver

from vehiclesregistrations.models import VehicleRegDocument


@receiver(post_save, sender=VehicleRegDocument)
def create_reg_document(instance, created, **kwargs):
    if created:
        VehicleRegDocument.objects.create(vehicle=instance)

from .models import Perfil
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Perfil)
def index_user(sender, instance, **kwargs):
    instance.indexing()

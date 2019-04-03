from django.db import models
from django.contrib.auth.models import User
from .search import UsuarioIndex
#from django.db.models.signals import post_save
#from django.dispatch import receiver



# Create your models here.
class Perfil(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='perfil')
    bio = models.CharField(max_length=255)
    web = models.URLField(max_length=255)
    # Python 3
    #def __str__(self):
    #    return self.usuario.username

    def indexing(self):
        obj = UsuarioIndex(
            meta={'id': self.id},
            usuario=self.usuario.username,
            bio=self.bio,
            web=self.web
        )
        obj.save(index='user-index')
        return obj.to_dict(include_meta=True)

'''@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfil.save()= models.OneToOneField
'''

from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Profile
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(pre_save,sender=User)
def create_hash_for_user(sender,instance,**kwargs):
    if not instance.pk:
        print(instance,'[[[[[[[[[[[[[[[[[[[[[')   
from django.db.models.signals import post_save
from django.dispatch import receiver
from auths.models import User, Profile

@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user = instance,
            fullname = instance.username
        )
    else:
        instance.profile.fullname = instance.username
        instance.profile.save()

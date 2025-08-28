from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuid.django_fields import ShortUUIDField
from django.utils.safestring import mark_safe

# Create your models here.

class User(AbstractUser):
    uid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="uid", alphabet="1234567890")

    username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    bio = models.TextField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    verified = models.BooleanField(default=False)
    image = models.ImageField(upload_to='profile/', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name_plural = 'Users'

    def save(self, *args, **kwargs):
        if self.email and not self.username:  
            self.username = self.email.split('@')[0]
        super().save(*args, **kwargs)

    def image(self):
        return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />')

    def __str__(self):
        return self.username or self.email or "Unnamed User"
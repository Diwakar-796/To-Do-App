from django.db import models
from auths.models import User
from shortuuid.django_fields import ShortUUIDField

# Create your models here.

LEVEL = (
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('hard', 'Hard'),
)

STATUS = (
    ('pending', 'Pending'),
    ('success', 'Success'),
    ('failed', 'Failed'),
)

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
       verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, default=None)
    level = models.CharField(choices=LEVEL, default='low', null=True, blank=True)
    
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
       verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title
    
class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    did = ShortUUIDField(unique=True, length=10, max_length=20, prefix="did", alphabet="1234567890")

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=50, default='pending')

    class Meta:
        verbose_name_plural = "Donations"

    def __str__(self):
        return self.did
    

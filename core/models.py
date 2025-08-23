from django.db import models
from auths.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
       verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title

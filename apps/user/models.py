from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=15)
    status = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(null=True, blank=True, default=timezone.now)

    def __str__(self):
        return self.name

from django.db import models
from django.conf import settings


class Venue(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    host_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    flat = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.flat}"

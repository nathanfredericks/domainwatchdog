from django.db import models
from django.contrib.auth.models import User


class Domain(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    updated_date = models.DateTimeField()
    creation_date = models.DateTimeField()
    registry_expiry_date = models.DateTimeField()
    registrar = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

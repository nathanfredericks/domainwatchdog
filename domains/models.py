from django.db import models
from django.contrib.auth.models import User


class Domain(models.Model):
    # Domain name (format: example.com)
    name = models.CharField(max_length=255)
    # Domain description (optionally set by user for display in dashboard)
    description = models.CharField(max_length=255, blank=True)

    # WHOIS properties
    # These properties are autofilled upon first commit.
    updated_date = models.DateTimeField(blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True)
    registry_expiry_date = models.DateTimeField(blank=True, null=True)
    registrar = models.CharField(max_length=255, blank=True)
    # If the WHOIS lookup is successful, this property will be switched to true.
    # If there is an error, the property will stay false and the user will be expected to enter domain properties manually.
    is_autofilled = models.BooleanField(default=False)

    # Domain owner
    # This refers to the model's owner in the application's database, **not the registration contact in the WHOIS database.**
    user = models.ForeignKey(User, on_delete=models.CASCADE)

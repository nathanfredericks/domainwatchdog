from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Domain(models.Model):
    """Model representing a registered domain name (e.g. example.com)"""
    # Domain name (format: example.com)
    name = models.CharField(max_length=255)
    # Domain description (optionally set by user for display in dashboard)
    description = models.CharField(max_length=255, blank=True)

    # WHOIS properties
    # These properties are autofilled upon first commit.
    updated_date = models.DateTimeField(blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True)
    registry_expiry_date = models.DateTimeField(blank=True, null=True)
    registrar = models.CharField(max_length=255, blank=True, null=True)

    # Last WHOIS lookup
    # This will be null when the model is first created, then switched to true after a successful WHOIS lookup.
    last_whois_lookup = models.DateTimeField(blank=True, null=True)

    # Domain owner
    # This refers to the model's owner in the application's database, **not the registration contact in the WHOIS database.**
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        """Returns the url to access a particular domain instance."""
        return reverse('domain-detail', args=[str(self.id)])
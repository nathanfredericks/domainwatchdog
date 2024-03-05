from celery import shared_task
from domains.models import Domain
import whois
from django.utils import timezone
from django.utils.timezone import make_aware

@shared_task(time_limit=15)
def whois_lookup(domain_id):
    try:
        domain = Domain.objects.get(pk=domain_id)
        w = whois.whois(domain.name)
        domain.updated_date = make_aware(w.updated_date)
        domain.creation_date = make_aware(w.creation_date)
        domain.registry_expiry_date = make_aware(w.expiration_date)
        domain.registrar = w.registrar
        domain.last_whois_lookup = timezone.now()
        domain.save()
    except Exception as e:
        print(e)

from celery import shared_task
from domains.models import Domain
import whois
from datetime import datetime


@shared_task(time_limit=15)
def whois_lookup(domain_id):
    try:
        domain = Domain.objects.get(pk=domain_id)
        w = whois.whois(domain.name)
        domain.updated_date = w.updated_date
        domain.creation_date = w.creation_date
        domain.registry_expiry_date = w.expiration_date
        domain.registrar = w.registrar
        domain.last_whois_lookup = datetime.now()
        domain.save()
    except Exception as e:
        print(e)

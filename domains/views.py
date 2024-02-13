from django.contrib.auth.mixins import LoginRequiredMixin
from domains import tasks
from domains.models import Domain
from django.views import generic


class DomainListView(LoginRequiredMixin, generic.ListView):
    login_url = "/login/"
    model = Domain


class DomainDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = "/login/"
    model = Domain


class DomainCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = "/login/"
    model = Domain
    fields = ["name", "description"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        domain = form.save()
        tasks.whois_lookup.delay(domain_id=domain.id)
        return super().form_valid(form)

from django.views import generic

from core.models import Policy

class PoliciesView(generic.ListView):
    # TemplateView used for our Policies page
    # core > templates > core/policies.html
    template_name = "core/policies.html"
    model = Policy
    # ListView, show first 10 results
    paginate_by = 10
    
    # query newest to oldest policies that are actived
    # https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views
    def get_queryset(self):
        return self.model.objects.active().order_by("-creation_date")
    
    
    
    
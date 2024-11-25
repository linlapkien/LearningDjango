from django.views import generic

from core.models import Event

class EventsView(generic.ListView):
    # TemplateView used for our Events page
    # core > templates > core/events.html
    template_name = "core/events.html"
    model = Event
    # ListView, show first 10 results
    paginate_by = 10
    
    # query newest to oldest policies that are actived
    # https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views
    def get_queryset(self):
        return self.model.objects.active().order_by("-creation_date")
    
    
    
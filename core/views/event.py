
from django.views import generic

from core.models import Event

class EventView(generic.DetailView):
    # DetailView used for our Event page
    # core > templates > core/event.html
    
    #https://docs.djangoproject.com/en/5.1/ref/class-based-views/generic-display/#:~:text=from%20django.utils%20import%20timezone%0Afrom%20django.views.generic.detail%20import%20DetailView
    template_name = "core/event.html"
    model = Event 
  
    def get_object(self):
        return self.model.objects.get(slug=self.kwargs['slug'])
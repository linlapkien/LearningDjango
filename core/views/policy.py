
from django.views import generic

from core.models import Policy

class PolicyView(generic.DetailView):
    # DetailView used for our Policy page
    # core > templates > core/policy.html
    
    #https://docs.djangoproject.com/en/5.1/ref/class-based-views/generic-display/#:~:text=from%20django.utils%20import%20timezone%0Afrom%20django.views.generic.detail%20import%20DetailView
    template_name = "core/policy.html"
    model = Policy 
  
    def get_object(self):
        return self.model.objects.get(slug=self.kwargs['slug'])
from django.views import generic

from core.models import Contact

from core.forms import ContactForm

class ContactView(generic.FormView):
    # FormView used for our Contact page
    # core > templates > core/contact.html
    
    template_name = "core/contact.html"
    form_class = ContactForm
    success_url = "/" 
from django.views import generic

class AboutView(generic.TemplateView):
    # TemplateView used for our About page
    # core > templates > core/about.html
    template_name = "core/about.html"

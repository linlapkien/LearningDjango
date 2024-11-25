from django.views import generic

class HomeView(generic.TemplateView):
    # TemplateView used for our home page
    # core > templates > core/index.html
    template_name = "core/index.html"

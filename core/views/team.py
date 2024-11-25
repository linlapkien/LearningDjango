from django.views import generic

class TeamView(generic.TemplateView):
    # TemplateView used for our Team page
    # core > templates > core/team.html
    template_name = "core/team.html"

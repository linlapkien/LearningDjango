from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("blogs/", views.BlogsView.as_view(), name="blogs"),
    path("events/", views.EventsView.as_view(), name="events"),
    path("team/", views.TeamView.as_view(), name="team"),
    path("policies/", views.PoliciesView.as_view(), name="policies"),
    
    
    path("blog/<str:slug>/", views.BlogView.as_view(), name="blog"),
    path("event/<str:slug>/", views.EventView.as_view(), name="event"),
    path("policy/<str:slug>/", views.PolicyView.as_view(), name="policy"),
]

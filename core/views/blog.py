from django.views import generic

from core.models import Blog

class BlogView(generic.DetailView):
    # DetailView used for our Blog page
    # core > templates > core/blog.html
    
    #https://docs.djangoproject.com/en/5.1/ref/class-based-views/generic-display/#:~:text=from%20django.utils%20import%20timezone%0Afrom%20django.views.generic.detail%20import%20DetailView
    template_name = "core/blog.html"
    model = Blog 
  
    def get_object(self):
        return self.model.objects.get(slug=self.kwargs['slug'])
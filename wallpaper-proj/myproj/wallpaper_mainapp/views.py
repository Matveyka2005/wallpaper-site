from django.views.generic import ListView
from .service import * 
from .models import * 


class HomePage(ListView):
    model = Image
    template_name = "wallpaper_mainapp/main.html"
    context_object_name = "images"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = get_objects(Category)
        return context
    
    
    
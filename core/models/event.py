from django.db import models

# utils>model import
from utils.model import Model

# https://django-extensions.readthedocs.io/en/latest/model_extensions.html#database-model-extensions
from django_extensions.db.models import ActivatorModel, TimeStampedModel, TitleSlugDescriptionModel

# https://pypi.org/project/django-ckeditor/6.5.1/#installation
from ckeditor.fields import RichTextField


class Event(ActivatorModel, TimeStampedModel, TitleSlugDescriptionModel, Model):
    
    class Meta:
        verbose_name_plural = "Our events" 
        
    body = RichTextField()

    
    

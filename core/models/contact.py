from django.db import models

# utils>model import
from utils.model import Model

# https://django-extensions.readthedocs.io/en/latest/model_extensions.html#database-model-extensions
from django_extensions.db.models import ActivatorModel, TimeStampedModel


class Contact(ActivatorModel, TimeStampedModel, Model):
    
    class Meta:
        verbose_name_plural = "Contacts via website" 
      
    # Contact form  
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    telephone = models.CharField(max_length=20)
    message = models.TextField(max_length=1000)
    
    
    
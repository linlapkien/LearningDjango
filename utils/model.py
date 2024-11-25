# Python imports
import uuid

# Django imports
from django.utils.translation import gettext_lazy as _
from django.db import models

class Model(models.Model):
    # We use this in EVERY db entry
    
    # https://www.geeksforgeeks.org/uuidfield-django-models/
    id = models.UUIDField(
        _('id'),
        primary_key=True,
        default=uuid.uuid4
    )
    
    class Meta:
        abstract = True
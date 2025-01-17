from django.contrib import admin
from core.models.contact import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'message', 'email', 'telephone')
    
    
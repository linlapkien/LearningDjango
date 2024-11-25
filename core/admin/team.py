from django.contrib import admin
from core.models.team import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    
    
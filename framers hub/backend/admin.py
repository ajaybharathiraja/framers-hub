from django.contrib import admin
from .models import ResearchEvent, TAMSurvey

@admin.register(ResearchEvent)
class ResearchEventAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'user', 'event_type')
    list_filter = ('event_type', 'timestamp')
    search_fields = ('user__username', 'event_type')

@admin.register(TAMSurvey)
class TAMSurveyAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'user', 'perceived_usefulness', 'perceived_ease_of_use')
    list_filter = ('created_at', 'perceived_usefulness', 'perceived_ease_of_use')
    search_fields = ('user__username',)

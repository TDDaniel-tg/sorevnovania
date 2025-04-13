from django.contrib import admin
from .models import Participant

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'city', 'weight_category', 'age', 'discipline', 'registration_date')
    search_fields = ('name', 'phone_number', 'city', 'discipline')
    list_filter = ('registration_date', 'city', 'discipline') 
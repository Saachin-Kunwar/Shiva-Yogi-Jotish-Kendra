# core/admin.py
from django.contrib import admin
from .models import Booking ,GuruProfile

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'service', 'consultation_date', 'created_at')
    search_fields = ('full_name', 'phone', 'email')

@admin.register(GuruProfile)
class GuruProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
    search_fields = ('name', 'title')
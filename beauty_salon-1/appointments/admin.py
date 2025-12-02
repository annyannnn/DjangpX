from django.contrib import admin
from .models import Appointment, AppointmentService

class AppointmentServiceInline(admin.TabularInline):
    model = AppointmentService
    extra = 0

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['booking_number', 'client_name', 'client_phone', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    inlines = [AppointmentServiceInline]

@admin.register(AppointmentService)
class AppointmentServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'service_price', 'specialist_name', 'appointment_date']
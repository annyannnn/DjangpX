from django.db import models
from django.utils import timezone

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('confirmed', 'Подтверждена'),
        ('completed', 'Завершена'),
        ('cancelled', 'Отменена'),
    ]
    
    booking_number = models.CharField(max_length=20, unique=True)
    salon_name = models.CharField(max_length=200)
    salon_address = models.CharField(max_length=300)
    
    client_name = models.CharField(max_length=100)
    client_phone = models.CharField(max_length=20)
    client_email = models.EmailField(blank=True, null=True)
    client_comment = models.TextField(blank=True)
    
    reminder = models.BooleanField(default=False)
    promocode_applied = models.BooleanField(default=False)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    original_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    final_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.booking_number} - {self.client_name}"

class AppointmentService(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='services')
    service_name = models.CharField(max_length=200)
    service_price = models.DecimalField(max_digits=10, decimal_places=2)
    service_duration = models.IntegerField(default=0)
    specialist_name = models.CharField(max_length=100)
    appointment_date = models.CharField(max_length=50)
    appointment_time = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.service_name} - {self.specialist_name}"
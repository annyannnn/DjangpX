from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Appointment, AppointmentService
from django.utils import timezone

@csrf_exempt
@require_http_methods(["POST"])
def book_appointment(request):
    try:
        data = json.loads(request.body)
        
        # Создаем запись
        appointment = Appointment(
            salon_name=data.get('salon', ''),
            salon_address=data.get('salonAddress', ''),
            client_name=data.get('clientName', ''),
            client_phone=data.get('clientPhone', ''),
            client_email=data.get('clientEmail', ''),
            client_comment=data.get('clientComment', ''),
            reminder=data.get('reminder', False),
            promocode_applied=data.get('promocodeApplied', False),
            discount_amount=data.get('discountAmount', 0),
            original_total=data.get('originalTotal', 0),
            final_total=data.get('finalTotal', 0)
        )
        
        # Генерируем номер записи
        appointment.booking_number = f"MS{timezone.now().strftime('%Y%m%d')}{Appointment.objects.count() + 1}"
        appointment.save()
        
        # Сохраняем услуги
        services = data.get('services', [])
        for service_data in services:
            AppointmentService.objects.create(
                appointment=appointment,
                service_name=service_data.get('name', ''),
                service_price=service_data.get('price', 0),
                service_duration=service_data.get('duration', 0),
                specialist_name=service_data.get('specialist', ''),
                appointment_date=service_data.get('date', ''),
                appointment_time=service_data.get('time', '')
            )
        
        return JsonResponse({
            'success': True,
            'booking_number': appointment.booking_number,
            'message': 'Запись успешно создана!'
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)

@require_http_methods(["GET"])
def health_check(request):
    return JsonResponse({'status': 'ok', 'service': 'Beauty Salon API'})
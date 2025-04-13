from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from .models import Participant
import json
import logging

logger = logging.getLogger(__name__)

def registration(request):
    return render(request, 'main/registr.html')

def participants_list(request):
    participants = Participant.objects.all()
    return render(request, 'main/spisok.html', {'participants': participants})

@csrf_exempt
def register_participant(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            logger.info(f"Получены данные: {data}")
            
            # Проверяем наличие всех необходимых полей
            required_fields = ['name', 'phone_number', 'city', 'weight_category', 'age', 'discipline']
            for field in required_fields:
                if field not in data:
                    logger.error(f"Отсутствует обязательное поле: {field}")
                    return JsonResponse({'status': 'error', 'message': f'Отсутствует обязательное поле: {field}'}, status=400)
            
            # Создаем объект участника
            participant = Participant(
                name=data['name'],
                phone_number=data['phone_number'],
                city=data['city'],
                weight_category=data['weight_category'],
                age=data['age'],
                discipline=data['discipline']
            )
            
            # Валидируем данные
            try:
                participant.full_clean()
            except ValidationError as e:
                logger.error(f"Ошибка валидации: {e}")
                return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
            
            # Сохраняем участника
            try:
                participant.save()
                logger.info(f"Участник успешно сохранен: {participant}")
                return JsonResponse({'status': 'success', 'message': 'Регистрация успешно завершена'})
            except Exception as e:
                logger.error(f"Ошибка при сохранении: {e}")
                return JsonResponse({'status': 'error', 'message': f'Ошибка при сохранении: {str(e)}'}, status=500)
                
        except json.JSONDecodeError as e:
            logger.error(f"Ошибка декодирования JSON: {e}")
            return JsonResponse({'status': 'error', 'message': 'Неверный формат JSON'}, status=400)
        except Exception as e:
            logger.error(f"Неожиданная ошибка: {e}")
            return JsonResponse({'status': 'error', 'message': f'Произошла ошибка: {str(e)}'}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Метод не поддерживается'}, status=405) 
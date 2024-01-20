# signals.py
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.apps import apps
from .models import Files
import os

@receiver(post_delete, sender=Files)
def delete_file_on_delete(sender, instance, **kwargs):
    # Удалить файл из системы при удалении объекта
    if instance.real_file_name:
        try:
            os.remove(instance.real_file_name)
        except FileNotFoundError:
            pass  # Файл уже удален или не существует

# Регистрация сигналов при загрузке приложения
app_config = apps.get_app_config('applications')  # Замените 'your_app_name' на имя вашего приложения
app_config.ready()

from django.core.management import BaseCommand
from users.models import User

"""Создали кастомную команду"""
class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email='django@mail.ru')
        user.set_password('')
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
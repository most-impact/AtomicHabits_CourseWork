from django.core.management import BaseCommand

from users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = CustomUser.objects.create(email='neykerez@gmail.com')
        user.set_password('89379540780Ar')
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
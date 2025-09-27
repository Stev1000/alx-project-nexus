# users/management/commands/createsu.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = os.getenv("DJANGO_SUPERUSER_USERNAME", "steven")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL", "nsanzestevo1@gmail.com")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "Neza0784@123!")

        try:
            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    "email": email,
                    "is_staff": True,
                    "is_superuser": True,
                },
            )
            # Always update user details
            user.email = email
            user.is_staff = True
            user.is_superuser = True
            user.set_password(password)   # Force reset password
            user.save()

            if created:
                self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created"))
            else:
                self.stdout.write(self.style.WARNING(f"Superuser '{username}' updated with new password"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Failed to create/update superuser: {e}"))

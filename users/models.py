from random import choices
from string import ascii_uppercase, digits

from django.db import models

from referral_system.settings import MAX_INVITE_CODE_LEN, MAX_PHONE_LEN


def generate_invite_code(length=MAX_INVITE_CODE_LEN):
    """Генерация уникального инвайт-кода для пользователя."""
    return ''.join(choices(ascii_uppercase + digits, k=length))


class User(models.Model):
    """Модель пользователя."""

    phone_number = models.CharField(max_length=MAX_PHONE_LEN, unique=True)
    invite_code = models.CharField(
        max_length=MAX_INVITE_CODE_LEN,
        unique=True,
        default=generate_invite_code
    )
    referred_by = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='referrals'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_number

import re

from django.core.exceptions import ValidationError


def email_validator(email):
    if not re.search(r'^[a-z\d_.-]{3,}\@[a-z_.-]+\.\w+$', email.strip(), re.I):
        raise ValidationError(f"Value {email} is not an email address.")


def phone_validator(phone):
    if not re.search(r'^\+?\d{10,12}$', phone.strip(), re.I):
        raise ValidationError(f"Value {phone} is not an email address.")

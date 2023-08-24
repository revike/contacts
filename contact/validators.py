import re
import phonenumbers

from django.core.exceptions import ValidationError


def validate_phone(value):
    """Validate for phone"""
    error = 'Invalid phone number format'
    try:
        pattern = r"^\+\d{8,15}$"
        number = phonenumbers.parse(value)
        if phonenumbers.is_valid_number(number) and re.search(pattern, value):
            return value
        raise ValidationError(error)
    except phonenumbers.NumberParseException:
        raise ValidationError(error)

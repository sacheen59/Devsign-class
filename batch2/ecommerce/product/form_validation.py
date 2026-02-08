from django.core.exceptions import ValidationError

def validate_less_than_0(value):
    if value <= 0:
        raise ValidationError("Value must be greater than 0.")
    return value
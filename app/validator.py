from django.core.exceptions import ValidationError

def validate_even(value):
    if value < 0:
        raise ValidationError(f'{value} is less then zero')
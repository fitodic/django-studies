from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_percent(value):
    if not 0 < value <= 100:
        raise ValidationError(
            _("Please set the percentage to a number between 0 and 100."),
            code="invalid_percentage",
        )

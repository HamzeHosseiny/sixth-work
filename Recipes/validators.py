import pint
from pint import UndefinedUnitError
from django.core.exceptions import ValidationError


def unit_validator(value):
    ureg = pint.UnitRegistry()
    try:
        single_unit = ureg[value]
    except UndefinedUnitError:
        raise ValidationError(f"{value} is not a defined unit.")
    except:
        raise ValidationError(f"something is wrong. try again.")
    
import pint
from django.conf import settings
from django.db import models
from .validators import unit_validator
from .utils import number_str_to_float

# Create your models here.

User = settings.AUTH_USER_MODEL

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 220)
    descriptions = models.TextField(blank = True, null = True)
    directions = models.TextField(blank = True, null = True)
    timestamps = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default = True)

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    name = models.CharField(max_length = 220)
    descriptipns = models.TextField(blank = True, null = True)
    directions = models.TextField(blank = True, null = True)
    quantity = models.CharField(max_length = 50)
    quantity_as_float = models.FloatField(blank = True, null = True)
    unit = models.CharField(max_length = 50, validators = [unit_validator])
    timestamps = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default = True)
    
    def convert_to_system(self, system = 'mks'):
        if self.quantity_as_float is None:
            return None
        ureg = pint.UnitRegistry(system = system)
        measurement = self.quantity_as_float * ureg[self.unit]
        return measurement
    
    def as_mks(self):
        measurement = self.convert_to_system(system = 'mks')
        return measurement.to_base_units()
    
    def as_imperial(self):
        measurement = self.convert_to_system(system = 'imperial')
        return measurement.to_base_units()
    
    def save(self, *args, **kwargs):
        qty = self.quantity
        qty_as_float, qty_as_float_success = number_str_to_float(qty)
        if qty_as_float_success:
            self.quantity_as_float = qty_as_float
        else:
            self.quantity_as_float = None
        super().save(*args, **kwargs)
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Income(models.Model):
    income_text = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1000000)])

    def __str__(self):
        return self.income_text
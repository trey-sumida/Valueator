from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Income(models.Model):
    income_text = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1000000)])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __int__(self):
        return self.income_text

class Topics(models.Model):
    topic_text = models.CharField(max_length=20)

    def __str__(self):
        return self.topic_text

class Expenditure(models.Model):
    expenditure_text = models.CharField(max_length=50)
    expenditure_price = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1000000)])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.expenditure_text




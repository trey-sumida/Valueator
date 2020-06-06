from django.contrib import admin

# Register your models here.
from .models import Income, Expenditure

admin.site.register(Income)
admin.site.register(Expenditure)

from django.contrib import admin

# Register your models here.
from .models import Income, Expenditure, Topics

admin.site.register(Income)
admin.site.register(Topics)
admin.site.register(Expenditure)

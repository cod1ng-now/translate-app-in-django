from django.contrib import admin
from .models import Lugat
# Register your models here.

class Lugatadmin(admin.ModelAdmin):
    list_display = ['inglizcha', 'uzbekcha']

admin.site.register(Lugat, Lugatadmin)
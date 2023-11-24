from django.contrib import admin
from .models import Barbearia

@admin.register(Barbearia)
class BarbeariaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'funcionarios')

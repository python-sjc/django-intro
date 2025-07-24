from django.contrib import admin
from .models import Fofoca

@admin.register(Fofoca)
class FofocaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'bairro', 'categoria', 'votos_confirmo', 'votos_mentira']

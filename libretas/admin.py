from django.contrib import admin
from .models import Supervisor, Conductor, EntregaLibreta

@admin.register(Supervisor)
class SupervisorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'usuario', 'get_email')
    search_fields = ('nombre', 'usuario__username', 'usuario__email')
    list_filter = ('usuario__is_active',)
    
    def get_email(self, obj):
        return obj.usuario.email if obj.usuario else '-'
    get_email.short_description = 'Email'

@admin.register(Conductor)
class ConductorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'supervisor')
    list_filter = ('supervisor',)
    search_fields = ('nombre', 'supervisor__nombre')

@admin.register(EntregaLibreta)
class EntregaLibretaAdmin(admin.ModelAdmin):
    list_display = ('conductor', 'fecha_entrega', 'mes', 'anio', 'semana', 'estado')
    list_filter = ('estado', 'mes', 'anio', 'semana', 'conductor__supervisor')
    search_fields = ('conductor__nombre',)
    date_hierarchy = 'fecha_entrega'
    ordering = ('-fecha_entrega',)

    fieldsets = (
        (None, {
            'fields': ('conductor', 'fecha_entrega')
        }),
        ('Información de la Libreta', {
            'fields': ('mes', 'anio', 'semana', 'estado')
        }),
    )
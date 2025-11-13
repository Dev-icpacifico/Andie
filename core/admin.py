from django.contrib import admin
# from .forms import AlertaForm
from .models import (
    Alerta, Departamento, Edificio, Persona, Piso, Proyecto, Resolucion,
    UnidadOperativa, ZonaExterior
)


@admin.register(Alerta)
class AlertaAdmin(admin.ModelAdmin):
    # Pequeños trucos para acortar el form
    # form = AlertaForm  # <<--- usa el form personalizado
    class Media:
        css = {
            'all': ('css/custom_admin.css',)  # Ruta dentro de static/
        }

    """readonly_fields = (
        "proyecto", "edificio", "departamento","piso"
    )"""
    list_per_page =10
    autocomplete_fields = ("proyecto", "edificio", "departamento", "colaborador_reporta", "piso",
                           "clasificacion_ia", "urgencia_ia", "clasificacion_val", "urgencia_val")
    search_fields = ("mensaje_alerta", "departamento__nombre", "edificio__nombre")
    list_display = (
    "numero_caso", "asignada_a", "colaborador_reporta", "unidad_operativa", "proyecto", "zona_exterior", "edificio",
    "piso", "estado_alerta", "fecha_apertura")
    list_filter = ("asignada_a","estado_alerta", "unidad_operativa", "fecha_apertura")
    ordering = ("-numero_caso",)


    fieldsets = (
        ("Datos de la alerta", {
            "fields": (
                ("proyecto", "edificio"), ("piso", "departamento"),
                ("recinto","zona_exterior"),
                ("mensaje_alerta",),
                ("fecha_apertura",),  # puedes agrupar en tuplas para líneas en horizontal

            )
        }),
        ("Partidas", {
            "fields": (("partida_faena", "partida_correcta"), ("clasificacion_ia", "urgencia_ia"),
                       ("clasificacion_val", "urgencia_val"), ("ubicacion_asignada", "observaciones_revision"))
        }),
        ("Asignación y estado", {
            "fields": (
                ("estado_alerta"),
                ("unidad_operativa", "colaborador_reporta"),
                ("fecha_asignacion",),
            )
        }),
    )


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('departamento_id', 'piso', 'numero')
    search_fields = ('numero',)


@admin.register(Edificio)
class EdificioAdmin(admin.ModelAdmin):
    list_display = ('edificio_id', 'proyecto', 'nombre')
    search_fields = ('nombre',)


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('persona_id', 'nombres', 'apellidos', 'email', 'cargo', 'activo')
    search_fields = ('nombres', 'apellidos', 'email')
    list_filter = ('activo',)


@admin.register(Piso)
class PisoAdmin(admin.ModelAdmin):
    list_display = ('piso_id', 'edificio', 'nivel')
    search_fields = ('nivel',)


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('proyecto_id', 'nombre', 'codigo', 'unidad_operativa')
    search_fields = ('nombre', 'codigo')


@admin.register(Resolucion)
class ResolucionAdmin(admin.ModelAdmin):
    list_display = ('resolucion_id', 'alerta', 'resolutor', 'estado_resolucion', 'fecha_inicio', 'fecha_cierre')


@admin.register(UnidadOperativa)
class UnidadOperativaAdmin(admin.ModelAdmin):
    list_display = ('unidad_operativa_id', 'nombre', 'codigo', 'activo')
    search_fields = ('nombre', 'codigo')
    list_filter = ('activo',)


@admin.register(ZonaExterior)
class ZonaExteriorAdmin(admin.ModelAdmin):
    list_display = ('zona_exterior_id', 'proyecto', 'nombre', 'tipo', 'activo')
    search_fields = ('nombre', 'tipo')
    list_filter = ('activo',)


# core/admin.py
from django.contrib import admin
from .models import CharlaDiaria

@admin.register(CharlaDiaria)
class CharlaDiariaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'locutor', 'seguridad', 'metas', 'motivacion')
    list_filter = ('fecha', 'locutor')

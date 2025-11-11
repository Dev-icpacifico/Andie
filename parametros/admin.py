from django.contrib import admin
from django.contrib import admin
from .models import (
    Adjunto, Aprobacion, AuditLog, CanalNotificacion, Cargo,
    Clasificacion, EstadoAlerta, EstadoResolucion,
    Jerarquia, Notificacion, Urgencia
)


# Register your models here.

@admin.register(Adjunto)
class AdjuntoAdmin(admin.ModelAdmin):
    list_display = ('adjunto_id', 'alerta', 'tipo', 'url', 'created_at')
    search_fields = ('tipo', 'url')
    list_filter = ('tipo',)


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('audit_id', 'entidad', 'entidad_id', 'accion', 'actor_id', 'fecha_evento')
    search_fields = ('entidad', 'accion')
    list_filter = ('accion',)


@admin.register(CanalNotificacion)
class CanalNotificacionAdmin(admin.ModelAdmin):
    list_display = ('canal_id', 'nombre')
    search_fields = ('nombre',)


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo_id', 'nombre', 'activo')
    search_fields = ('nombre',)
    list_filter = ('activo',)


@admin.register(Clasificacion)
class ClasificacionAdmin(admin.ModelAdmin):
    list_display = ('clasificacion_id', 'nombre', 'activo')
    search_fields = ('nombre',)
    list_filter = ('activo',)


@admin.register(EstadoAlerta)
class EstadoAlertaAdmin(admin.ModelAdmin):
    list_display = ('estado_alerta_id', 'codigo', 'descripcion')
    search_fields = ('codigo', 'descripcion')


@admin.register(EstadoResolucion)
class EstadoResolucionAdmin(admin.ModelAdmin):
    list_display = ('estado_resolucion_id', 'codigo', 'descripcion')
    search_fields = ('codigo', 'descripcion')


@admin.register(Urgencia)
class UrgenciaAdmin(admin.ModelAdmin):
    list_display = ('urgencia_id', 'nombre', 'nivel', 'activo')
    search_fields = ('nombre',)
    list_filter = ('activo',)


@admin.register(Jerarquia)
class JerarquiaAdmin(admin.ModelAdmin):
    list_display = ('jerarquia_id', 'colaborador', 'supervisor', 'nivel', 'activo')
    list_filter = ('activo',)


@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    list_display = ('notificacion_id', 'alerta', 'destinatario', 'canal', 'estado_envio', 'fecha_envio')
    search_fields = ('mensaje_enviado', 'tipo')
    list_filter = ('estado_envio', 'tipo')


@admin.register(Aprobacion)
class AprobacionAdmin(admin.ModelAdmin):
    list_display = ('aprobacion_id', 'alerta', 'aprobador', 'resultado', 'fecha_aprobacion')
    search_fields = ('comentario',)
    list_filter = ('resultado',)

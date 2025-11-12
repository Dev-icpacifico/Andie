from django.db import models
# Create your models here.

class Adjunto(models.Model):
    adjunto_id = models.UUIDField(primary_key=True)
    alerta = models.ForeignKey('core.Alerta', models.DO_NOTHING)
    tipo = models.TextField()
    url = models.TextField()
    metadata = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'adjunto'
        # managed = False


class AuditLog(models.Model):
    audit_id = models.UUIDField(primary_key=True)
    entidad = models.TextField()
    entidad_id = models.UUIDField()
    accion = models.TextField()
    actor_id = models.UUIDField(blank=True, null=True)
    detalle = models.JSONField(blank=True, null=True)
    fecha_evento = models.DateTimeField()

    class Meta:
        db_table = 'audit_log'
        # managed = False


class CanalNotificacion(models.Model):
    canal_id = models.UUIDField(primary_key=True)
    nombre = models.TextField(unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'canal_notificacion'
        # managed = False


class Cargo(models.Model):
    cargo_id = models.UUIDField(primary_key=True)
    nombre = models.TextField(unique=True)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'cargo'
        # managed = False


class Clasificacion(models.Model):
    clasificacion_id = models.UUIDField(primary_key=True)
    nombre = models.TextField(unique=True)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'clasificacion'
        # managed = False


class EstadoAlerta(models.Model):
    estado_alerta_id = models.UUIDField(primary_key=True)
    codigo = models.TextField(unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.codigo

    class Meta:
        db_table = 'estado_alerta'
        # managed = False


class EstadoResolucion(models.Model):
    estado_resolucion_id = models.UUIDField(primary_key=True)
    codigo = models.TextField(unique=True)
    descripcion = models.TextField()

    class Meta:
        db_table = 'estado_resolucion'
        # managed = False


class Urgencia(models.Model):
    urgencia_id = models.UUIDField(primary_key=True)
    nombre = models.TextField(unique=True)
    nivel = models.SmallIntegerField()
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'urgencia'
        # managed = False


class Jerarquia(models.Model):
    jerarquia_id = models.UUIDField(primary_key=True)
    colaborador = models.ForeignKey('core.Persona', models.DO_NOTHING)
    supervisor = models.ForeignKey('core.Persona', models.DO_NOTHING, related_name='jerarquia_supervisor_set')
    nivel = models.SmallIntegerField()
    activo = models.BooleanField()

    class Meta:
        db_table = 'jerarquia'
        unique_together = (('colaborador', 'nivel'),)
        # managed = False


class Notificacion(models.Model):
    notificacion_id = models.UUIDField(primary_key=True)
    alerta = models.ForeignKey('core.Alerta', models.DO_NOTHING)
    destinatario = models.ForeignKey('core.Persona', models.DO_NOTHING)
    canal = models.ForeignKey(CanalNotificacion, models.DO_NOTHING)
    tipo = models.TextField()
    mensaje_enviado = models.TextField()
    estado_envio = models.TextField()
    trace_id = models.TextField(blank=True, null=True)
    fecha_envio = models.DateTimeField()

    class Meta:
        db_table = 'notificacion'
        # managed = False


class Aprobacion(models.Model):
    aprobacion_id = models.UUIDField(primary_key=True)
    alerta = models.OneToOneField('core.Alerta', models.DO_NOTHING)
    aprobador = models.ForeignKey('core.Persona', models.DO_NOTHING)
    cargo_aprobador = models.TextField(blank=True, null=True)
    resultado = models.TextField()
    comentario = models.TextField(blank=True, null=True)
    fecha_aprobacion = models.DateTimeField()

    class Meta:
        db_table = 'aprobacion'
        # managed = False

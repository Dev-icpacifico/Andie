import uuid

from django.db import models
# Create your models here.

class Adjunto(models.Model):
    adjunto_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alerta = models.ForeignKey('core.Alerta', models.DO_NOTHING)
    tipo = models.CharField(max_length=50,unique=True, help_text="Ej:Imagen")
    url = models.TextField()
    metadata = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'adjunto'


class AuditLog(models.Model):
    audit_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    entidad = models.CharField(max_length=50,unique=True)
    entidad_id = models.UUIDField()
    accion = models.TextField()
    actor_id = models.UUIDField(blank=True, null=True)
    detalle = models.JSONField(blank=True, null=True)
    fecha_evento = models.DateTimeField()

    class Meta:
        db_table = 'audit_log'


class CanalNotificacion(models.Model):
    canal_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'canal_notificacion'


class Cargo(models.Model):
    cargo_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50,unique=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'cargo'


class Clasificacion(models.Model):
    clasificacion_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=60,unique=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'clasificacion'


class EstadoAlerta(models.Model):
    estado_alerta_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(max_length=50,unique=True)
    descripcion = models.CharField(max_length=80,unique=True)

    def __str__(self):
        return self.codigo

    class Meta:
        db_table = 'estado_alerta'


class EstadoResolucion(models.Model):
    estado_resolucion_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(max_length=50,unique=True)
    descripcion = models.CharField(max_length=80,unique=True)

    class Meta:
        db_table = 'estado_resolucion'


class Urgencia(models.Model):
    urgencia_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50,unique=True)
    nivel = models.SmallIntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'urgencia'


class Jerarquia(models.Model):
    jerarquia_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    colaborador = models.ForeignKey('core.Persona', models.DO_NOTHING)
    supervisor = models.ForeignKey('core.Persona', models.DO_NOTHING, related_name='jerarquia_supervisor_set')
    nivel = models.SmallIntegerField()
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'jerarquia'
        unique_together = (('colaborador', 'nivel'),)


class Notificacion(models.Model):
    notificacion_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alerta = models.ForeignKey('core.Alerta', models.DO_NOTHING)
    destinatario = models.ForeignKey('core.Persona', models.DO_NOTHING)
    canal = models.ForeignKey(CanalNotificacion, models.DO_NOTHING)
    tipo = models.CharField(max_length=50,unique=True)
    mensaje_enviado = models.TextField()
    estado_envio = models.CharField(max_length=50,unique=True)
    trace_id = models.TextField(blank=True, null=True)
    fecha_envio = models.DateTimeField()

    class Meta:
        db_table = 'notificacion'


class Aprobacion(models.Model):
    aprobacion_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alerta = models.OneToOneField('core.Alerta', models.DO_NOTHING)
    aprobador = models.ForeignKey('core.Persona', models.DO_NOTHING)
    cargo_aprobador = models.TextField(blank=True, null=True)
    resultado = models.TextField()
    comentario = models.TextField(blank=True, null=True)
    fecha_aprobacion = models.DateTimeField()

    class Meta:
        db_table = 'aprobacion'
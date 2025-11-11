import uuid

from django.db import models

from parametros.models import EstadoResolucion, Cargo


class Alerta(models.Model):
    alerta_id = models.UUIDField(primary_key=True)
    fecha_apertura = models.DateTimeField()
    proyecto = models.ForeignKey('Proyecto', models.DO_NOTHING, blank=True, null=True)
    edificio = models.ForeignKey('Edificio', models.DO_NOTHING, blank=True, null=True)
    piso = models.ForeignKey('Piso', models.DO_NOTHING, blank=True, null=True)
    departamento = models.ForeignKey('Departamento', models.DO_NOTHING, blank=True, null=True)
    recinto = models.TextField(blank=True, null=True)
    mensaje_alerta = models.TextField()
    clasificacion_ia = models.ForeignKey('parametros.Clasificacion', models.DO_NOTHING, blank=True, null=True)
    urgencia_ia = models.ForeignKey('parametros.Urgencia', models.DO_NOTHING, blank=True, null=True)
    clasificacion_val = models.ForeignKey('parametros.Clasificacion', models.DO_NOTHING, related_name='alerta_clasificacion_val_set', blank=True, null=True)
    urgencia_val = models.ForeignKey('parametros.Urgencia', models.DO_NOTHING, related_name='alerta_urgencia_val_set', blank=True, null=True)
    partida_faena = models.CharField(max_length=80,blank=True, null=True)
    partida_correcta = models.BooleanField(blank=True, null=True)
    ubicacion_asignada = models.BooleanField(blank=True, null=True)
    observaciones_revision = models.TextField(blank=True, null=True)
    estado_alerta = models.ForeignKey('parametros.EstadoAlerta', models.DO_NOTHING)
    unidad_operativa = models.ForeignKey('UnidadOperativa', models.DO_NOTHING, blank=True, null=True)
    colaborador_reporta = models.ForeignKey('Persona', models.DO_NOTHING)
    fecha_asignacion = models.DateTimeField(blank=True, null=True)
    fecha_resolucion = models.DateTimeField(blank=True, null=True)
    fecha_aprobacion = models.DateTimeField(blank=True, null=True)
    fecha_cierre = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    zona_exterior = models.ForeignKey('ZonaExterior', models.DO_NOTHING, blank=True, null=True)
    numero_caso = models.IntegerField(unique=True)
    asignada_a = models.ForeignKey('Persona', models.DO_NOTHING, related_name='alerta_asignada_a_set', blank=True, null=True)

    def __str__(self):
        return str(self.numero_caso)

    class Meta:
        db_table = 'alerta'



class Persona(models.Model):
    persona_id = models.UUIDField(primary_key=True)
    rut = models.TextField(blank=True, null=True)
    nombres = models.TextField()
    apellidos = models.TextField()
    email = models.TextField(blank=True, null=True)
    telefono_wsp = models.TextField(blank=True, null=True)
    tipo = models.TextField()
    cargo = models.ForeignKey(Cargo, models.DO_NOTHING, blank=True, null=True)
    unidad_operativa = models.ForeignKey('UnidadOperativa', models.DO_NOTHING, blank=True, null=True)
    activo = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    supervisor = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.nombres +" "+ self.apellidos

    class Meta:
        db_table = 'persona'

class UnidadOperativa(models.Model):
    unidad_operativa_id = models.UUIDField(primary_key=True)
    nombre = models.TextField(unique=True)
    codigo = models.TextField(blank=True, null=True)
    ubicacion = models.TextField(blank=True, null=True)
    activo = models.BooleanField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'unidad_operativa'


class Proyecto(models.Model):
    proyecto_id = models.UUIDField(primary_key=True)
    nombre = models.TextField(unique=True)
    codigo = models.TextField(blank=True, null=True)
    unidad_operativa = models.ForeignKey('UnidadOperativa', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'proyecto'


class ZonaExterior(models.Model):
    zona_exterior_id = models.UUIDField(primary_key=True)
    proyecto = models.ForeignKey(Proyecto, models.DO_NOTHING)
    nombre = models.TextField()
    tipo = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'zona_exterior'
        unique_together = (('proyecto', 'nombre'),)

class Edificio(models.Model):
    edificio_id = models.UUIDField(primary_key=True)
    proyecto = models.ForeignKey('Proyecto', models.DO_NOTHING)
    nombre = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'edificio'
        unique_together = (('proyecto', 'nombre'),)

class Departamento(models.Model):
    departamento_id = models.UUIDField(primary_key=True)
    piso = models.ForeignKey('Piso', models.DO_NOTHING)
    numero = models.TextField()

    def __str__(self):
        return self.numero

    class Meta:
        db_table = 'departamento'
        unique_together = (('piso', 'numero'),)

class Resolucion(models.Model):
    resolucion_id = models.UUIDField(primary_key=True)
    alerta = models.OneToOneField(Alerta, models.DO_NOTHING)
    resolutor = models.ForeignKey(Persona, models.DO_NOTHING)
    cargo_resolutor = models.TextField(blank=True, null=True)
    mensaje_solucion = models.TextField(blank=True, null=True)
    estado_resolucion = models.ForeignKey(EstadoResolucion, models.DO_NOTHING)
    requiere_mejora = models.BooleanField(blank=True, null=True)
    observacion_mejora = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_cierre = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'resolucion'

class Piso(models.Model):
    piso_id = models.UUIDField(primary_key=True)
    edificio = models.ForeignKey(Edificio, models.DO_NOTHING)
    nivel = models.TextField()

    def __str__(self):
        return self.nivel

    class Meta:
        db_table = 'piso'
        unique_together = (('edificio', 'nivel'),)



class CharlaDiaria(models.Model):
    charla_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    locutor = models.ForeignKey('core.Persona', on_delete=models.DO_NOTHING)
    fecha = models.DateField()

    jornada_anterior = models.BooleanField(default=False,blank=True, null=True)
    seguridad = models.BooleanField(default=False,blank=True, null=True)
    contexto = models.BooleanField(default=False,blank=True, null=True)
    condiciones = models.BooleanField(default=False,blank=True, null=True)
    metas = models.BooleanField(default=False,blank=True, null=True)
    sugerencias = models.BooleanField(default=False,blank=True, null=True)
    motivacion = models.BooleanField(default=False,blank=True, null=True)

    charla_completa = models.TextField()
    sugerencias_mejoras = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True, null=True)

    class Meta:
        db_table = 'charla_diaria'
        unique_together = ('locutor', 'fecha')
        ordering = ['-fecha']

    def __str__(self):
        return f"Charla {self.fecha} - {self.locutor}"

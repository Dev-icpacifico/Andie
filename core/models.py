import uuid

from django.db import models

from parametros.models import EstadoResolucion, Cargo


class Alerta(models.Model):
    alerta_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha_apertura = models.DateTimeField()
    proyecto = models.ForeignKey('Proyecto', models.DO_NOTHING, blank=True, null=True)
    edificio = models.ForeignKey('Edificio', models.DO_NOTHING, blank=True, null=True)
    piso = models.ForeignKey('Piso', models.DO_NOTHING, blank=True, null=True)
    departamento = models.ForeignKey('Departamento', models.DO_NOTHING, blank=True, null=True)
    recinto = models.CharField(max_length=50,blank=True, null=True)
    mensaje_alerta = models.TextField()
    clasificacion_ia = models.ForeignKey('parametros.Clasificacion', models.DO_NOTHING, blank=True, null=True)
    urgencia_ia = models.ForeignKey('parametros.Urgencia', models.DO_NOTHING, blank=True, null=True)
    clasificacion_val = models.ForeignKey('parametros.Clasificacion', models.DO_NOTHING, related_name='alerta_clasificacion_val_set', blank=True, null=True)
    urgencia_val = models.ForeignKey('parametros.Urgencia', models.DO_NOTHING, related_name='alerta_urgencia_val_set', blank=True, null=True)
    partida_faena = models.CharField(max_length=80,blank=True)
    partida_correcta = models.BooleanField(blank=True, default=False)
    ubicacion_asignada = models.BooleanField(blank=True, default=False)
    observaciones_revision = models.TextField(blank=True)
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
    persona_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rut = models.CharField(max_length=12, help_text="Ej:11.111.111-1")
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    email = models.EmailField()
    telefono_wsp = models.CharField(max_length=12, help_text="Ej:+56912345678")
    tipo = models.CharField(max_length=30)
    cargo = models.ForeignKey(Cargo, models.DO_NOTHING)
    unidad_operativa = models.ForeignKey('UnidadOperativa', models.DO_NOTHING)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True)
    supervisor = models.ForeignKey('Persona', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return str(self.nombres) +" "+ str(self.apellidos)

    class Meta:
        db_table = 'persona'

class UnidadOperativa(models.Model):
    unidad_operativa_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(unique=True, max_length=50)
    codigo = models.CharField(max_length=6,blank=True)
    ubicacion = models.CharField(max_length=50, blank=True)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField()

    def __str__(self):
        return str(self.nombre)

    class Meta:
        db_table = 'unidad_operativa'


class Proyecto(models.Model):
    proyecto_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50,unique=True)
    codigo = models.CharField(max_length=6,unique=True)
    unidad_operativa = models.ForeignKey('UnidadOperativa', models.DO_NOTHING)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'proyecto'


class ZonaExterior(models.Model):
    zona_exterior_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    proyecto = models.ForeignKey(Proyecto, models.DO_NOTHING)
    nombre = models.CharField(max_length=50,unique=True)
    tipo = models.CharField(max_length=50,unique=True)
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'zona_exterior'
        unique_together = (('proyecto', 'nombre'),)

class Edificio(models.Model):
    edificio_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    proyecto = models.ForeignKey('Proyecto', models.DO_NOTHING)
    nombre = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'edificio'
        unique_together = (('proyecto', 'nombre'),)

class Departamento(models.Model):
    departamento_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    piso = models.ForeignKey('Piso', models.DO_NOTHING)
    numero = models.CharField(max_length=4,unique=True, help_text="Ej:101")

    def __str__(self):
        return self.numero

    class Meta:
        db_table = 'departamento'
        unique_together = (('piso', 'numero'),)

class Resolucion(models.Model):
    resolucion_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alerta = models.OneToOneField(Alerta, models.DO_NOTHING)
    resolutor = models.ForeignKey(Persona, models.DO_NOTHING)
    cargo_resolutor = models.CharField(max_length=50,unique=True, blank=True)
    mensaje_solucion = models.CharField(max_length=50,unique=True, blank=True)
    estado_resolucion = models.ForeignKey(EstadoResolucion, models.DO_NOTHING)
    requiere_mejora = models.BooleanField(blank=True, default=False)
    observacion_mejora = models.TextField(blank=True)
    fecha_inicio = models.DateTimeField(blank=True)
    fecha_cierre = models.DateTimeField(blank=True)

    class Meta:
        db_table = 'resolucion'

class Piso(models.Model):
    piso_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    edificio = models.ForeignKey(Edificio, models.DO_NOTHING)
    nivel = models.CharField(max_length=3,unique=True, help_text="Ej:1")

    def __str__(self):
        return self.nivel

    class Meta:
        db_table = 'piso'
        unique_together = (('edificio', 'nivel'),)



class CharlaDiaria(models.Model):
    charla_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    locutor = models.ForeignKey('core.Persona', on_delete=models.DO_NOTHING)
    fecha = models.DateField()

    jornada_anterior = models.BooleanField(default=False,blank=True)
    seguridad = models.BooleanField(default=False,blank=True)
    contexto = models.BooleanField(default=False,blank=True)
    condiciones = models.BooleanField(default=False,blank=True)
    metas = models.BooleanField(default=False,blank=True)
    sugerencias = models.BooleanField(default=False,blank=True)
    motivacion = models.BooleanField(default=False,blank=True)

    charla_completa = models.TextField()
    sugerencias_mejoras = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True)

    class Meta:
        db_table = 'charla_diaria'
        unique_together = ('locutor', 'fecha')
        ordering = ['-fecha']

    def __str__(self):
        return f"Charla {self.fecha} - {self.locutor}"

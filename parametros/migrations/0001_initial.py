# parametros/migrations/0001_initial.py
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('core', '0002_auto_20251028_1244'),  # <- solo hasta core.0002
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                # --- Define en el STATE los modelos movidos (tablas YA existen) ---

                migrations.CreateModel(
                    name='AuditLog',
                    fields=[
                        ('audit_id', models.UUIDField(primary_key=True, serialize=False)),
                        ('entidad', models.TextField()),
                        ('entidad_id', models.UUIDField()),
                        ('accion', models.TextField()),
                        ('actor_id', models.UUIDField(blank=True, null=True)),
                        ('detalle', models.JSONField(blank=True, null=True)),
                        ('fecha_evento', models.DateTimeField()),
                    ],
                    options={'db_table': 'audit_log'},
                ),

                migrations.CreateModel(
                    name='CanalNotificacion',
                    fields=[
                        ('canal_id', models.UUIDField(primary_key=True, serialize=False)),
                        ('nombre', models.TextField(unique=True)),
                    ],
                    options={'db_table': 'canal_notificacion'},
                ),

                migrations.CreateModel(
                    name='Cargo',
                    fields=[
                        ('cargo_id', models.UUIDField(primary_key=True, serialize=False)),
                        ('nombre', models.TextField(unique=True)),
                        ('activo', models.BooleanField()),
                    ],
                    options={'db_table': 'cargo'},
                ),

                migrations.CreateModel(
                    name='Clasificacion',
                    fields=[
                        ('clasificacion_id', models.UUIDField(primary_key=True, serialize=False)),
                        ('nombre', models.TextField(unique=True)),
                        ('activo', models.BooleanField()),
                    ],
                    options={'db_table': 'clasificacion'},
                ),

                migrations.CreateModel(
                    name='EstadoAlerta',
                    fields=[
                        ('estado_alerta_id', models.UUIDField(primary_key=True, serialize=False)),
                        ('codigo', models.TextField(unique=True)),
                        ('descripcion', models.TextField()),
                    ],
                    options={'db_table': 'estado_alerta'},
                ),

                migrations.CreateModel(
                    name='EstadoResolucion',
                    fields=[
                        ('estado_resolucion_id', models.UUIDField(primary_key=True, serialize=False)),
                        ('codigo', models.TextField(unique=True)),
                        ('descripcion', models.TextField()),
                    ],
                    options={'db_table': 'estado_resolucion'},
                ),

                migrations.CreateModel(
                    name='Urgencia',
                    fields=[
                        ('urgencia_id', models.UUIDField(primary_key=True, serialize=False)),
                        ('nombre', models.TextField(unique=True)),
                        ('nivel', models.SmallIntegerField()),
                        ('activo', models.BooleanField()),
                    ],
                    options={'db_table': 'urgencia'},
                ),

                migrations.CreateModel(
                    name='Adjunto',
                    fields=[
                        ('adjunto_id', models.UUIDField(primary_key=True, serialize=False)),
                        ('tipo', models.TextField()),
                        ('url', models.TextField()),
                        ('metadata', models.JSONField(blank=True, null=True)),
                        ('created_at', models.DateTimeField()),
                        ('alerta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.alerta')),
                    ],
                    options={'db_table': 'adjunto'},
                ),

                migrations.CreateModel(
                    name='Aprobacion',
                    fields=[
                        ('aprobacion_id', models.UUIDField(primary_key=True, serialize=False)),
                        ('cargo_aprobador', models.TextField(blank=True, null=True)),
                        ('resultado', models.TextField()),
                        ('comentario', models.TextField(blank=True, null=True)),
                        ('fecha_aprobacion', models.DateTimeField()),
                        ('alerta', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='core.alerta')),
                        ('aprobador', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.persona')),
                    ],
                    options={'db_table': 'aprobacion'},
                ),

                migrations.CreateModel(
                    name='Notificacion',
                    fields=[
                        ('notificacion_id', models.UUIDField(primary_key=True, serialize=False)),
                        ('tipo', models.TextField()),
                        ('mensaje_enviado', models.TextField()),
                        ('estado_envio', models.TextField()),
                        ('trace_id', models.TextField(blank=True, null=True)),
                        ('fecha_envio', models.DateTimeField()),
                        ('alerta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.alerta')),
                        ('canal', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='parametros.canalnotificacion')),
                        ('destinatario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.persona')),
                    ],
                    options={'db_table': 'notificacion'},
                ),

                migrations.CreateModel(
                    name='Jerarquia',
                    fields=[
                        ('jerarquia_id', models.UUIDField(primary_key=True, serialize=False)),
                        ('nivel', models.SmallIntegerField()),
                        ('activo', models.BooleanField()),
                        ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.persona')),
                        ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='jerarquia_supervisor_set', to='core.persona')),
                    ],
                    options={'db_table': 'jerarquia', 'unique_together': {('colaborador', 'nivel')}},
                ),
            ],
            database_operations=[
                # vacío: NO crear/alterar/borrar tablas reales (ya existen)
            ],
        ),
    ]

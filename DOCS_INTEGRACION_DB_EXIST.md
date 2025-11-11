# Documentación de Integración de Django con Base de Datos Existente

## Situación Inicial

Se contaba con una base de datos PostgreSQL utilizada por **n8n** y **pgAdmin** para gestionar flujos de trabajo. La base de datos:

- Contiene tablas con **PK y FK en formato UUID**.  
- No usa tipos avanzados de PostgreSQL como `JSONB` especiales, `ARRAY`, `ENUM custom`, `hstore` o PostGIS.  
- Tiene triggers y constraints ya definidos.  
- No se modificaba el esquema automáticamente por ninguna aplicación externa.  
- Los datos existentes son consistentes y los `NULL` son necesarios en ciertos campos.  
- Se requiere acceso concurrente desde Django y n8n a las mismas tablas.

---

## Planteamiento

Se decidió integrar **Django** para:

- Gestionar el esquema de la base de datos (migraciones futuras).  
- Crear APIs y panel de administración.  
- Implementar lógica de negocio y ETL.  
- Posibilidad de añadir nuevas tablas o columnas desde Django en el futuro.

Se buscó hacerlo **sobre la base de datos existente**, sin crear un staging ni duplicar los datos, manteniendo la integridad de las tablas y relaciones.

---

## Objetivos

1. Tener un **proyecto Django** conectado a la base existente.  
2. Poder **generar migraciones futuras** desde Django.  
3. Mantener el esquema y los datos existentes intactos.  
4. Permitir acceso concurrente desde Django y otras aplicaciones.  
5. Documentar todo el proceso para reproducibilidad y referencia futura.

---

## Plan de Acción Ejecutado

### Paso 1: Preparación de entorno

- Crear un entorno virtual en Python (`venv`).  
- Instalar Django y psycopg2 para conexión PostgreSQL.

### Paso 2: Inspección de la base de datos

- Ejecutar `python manage.py inspectdb` para generar modelos Django a partir de la base existente.  
- Guardar la salida en `core/models.py`.  

### Paso 3: Limpieza de `models.py`

- Detectar y eliminar **null bytes** introducidos por `inspectdb` o codificación incorrecta en Windows.  
- Guardar el archivo en **UTF-8 sin BOM**.  

### Paso 4: Ajuste de campos especiales

- `AutoField` que no es PK fue reemplazado por `IntegerField(unique=True)`.  
- Se mantuvo `UUIDField(primary_key=True)` en las PK existentes.  

Ejemplo:

```python
class Alerta(models.Model):
    alerta_id = models.UUIDField(primary_key=True)
    numero_caso = models.IntegerField(unique=True)
````

### Paso 5: Migración inicial

* Ejecutar `python manage.py makemigrations core` para generar la migración inicial vacía que Django pueda gestionar.
* Ejecutar `python manage.py migrate` para aplicar la migración y conectar Django con la base existente.

### Paso 6: Decisión sobre triggers y funciones

* Se decidió **no versionar triggers y funciones con RunSQL**, porque:

  * Ya existen en la base de datos.
  * No es necesario que Django los gestione por ahora.

Esto simplifica la integración y permite centrarse en gestión de tablas y datos.

---

## Resultados

* Django ahora está conectado a la base de datos existente.
* Los modelos reflejan todas las tablas actuales, relaciones FK y constraints básicas.
* Las migraciones futuras se pueden crear desde Django sin afectar datos existentes.
* Se dejó documentado el proceso completo para referencia futura.

---

## Consideraciones Futuras

* En caso de agregar triggers o funciones nuevas que deban ser reproducibles, se pueden versionar mediante migraciones con `RunSQL`.
* Es recomendable revisar los índices compuestos y constraints CHECK si se añaden nuevas migraciones que afecten integridad.
* Mantener consistencia de tipos UUID y secuencias numéricas si se agregan nuevos campos `IntegerField` como `numero_caso`.

---

**Fin de la Documentación**


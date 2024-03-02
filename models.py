from tortoise import fields, models


class Alumnos(models.Model):
    id = fields.IntField(pk=True)
    Nombre = fields.CharField(max_length=255)
    Telefono = fields.IntField(null=True)
    Direccion = fields.CharField(max_length=255, null=True)

class Autores(models.Model):
    id = fields.IntField(pk=True)
    Nombre = fields.CharField(max_length=255)

class Libros(models.Model):
    id = fields.IntField(pk=True)
    Titulo = fields.CharField(max_length=255)
    ISBN = fields.IntField(default="0")
    Editorial = fields.CharField(max_length=255)
    Paginas = fields.IntField(default="0")

class Escribe(models.Model):
    id = fields.IntField(pk=True)
    AutorId: fields.ForeignKeyRelation[Autores] = fields.ForeignKeyField(
        "models.Autores", related_name="Escribe"
    )
    LibroId: fields.ForeignKeyRelation[Libros] = fields.ForeignKeyField(
        "models.Libros", related_name="Escribe"
    )

class Ejemplares(models.Model):
    id = fields.IntField(pk=True)
    Localizacion = fields.CharField(max_length=255)
    LibroId: fields.ForeignKeyRelation[Libros] = fields.ForeignKeyField(
        "models.Libros", related_name="Ejemplares"
    )

class Saca(models.Model):
    id = fields.IntField(pk=True)
    EjemplarId: fields.ForeignKeyRelation[Ejemplares] = fields.ForeignKeyField(
        "models.Ejemplares", related_name="Saca"
    )
    AlumnoId: fields.ForeignKeyRelation[Alumnos] = fields.ForeignKeyField(
        "models.Alumnos", related_name="Saca"
    )
    FechaPrestamo = fields.DateField()
    FechaDevolucion = fields.DateField()


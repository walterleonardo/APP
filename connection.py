import sqlite3


class Coneccion():
    def __init__(self) -> None:
        self.coneccion = sqlite3.connect('./db.sqlite3')
        self.create_database_alumnos(self.coneccion)
        self.create_database_libros(self.coneccion)
        self.create_database_autores(self.coneccion)
        self.create_database_escribe(self.coneccion)
        self.create_database_ejemplares(self.coneccion)
        self.create_database_saca(self.coneccion)
        # Convertir resultado en diccionario
        def row_to_dict(cursor: sqlite3.Cursor, row: sqlite3.Row) -> dict:
            data = {}
            for idx, col in enumerate(cursor.description):
                data[col[0]] = row[idx]
            return data
        self.coneccion.row_factory = row_to_dict

        
    def create_database_alumnos(self, coneccion):
        c = coneccion.cursor()
        sql = '''CREATE TABLE IF NOT EXISTS alumnos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        telefono TEXT,
        direccion TEXT
        )'''
        c.execute(sql)
        coneccion.commit()

    def create_database_libros(self, coneccion):
        c = coneccion.cursor()
        sql = '''CREATE TABLE IF NOT EXISTS libros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        isbn INTEGER,
        editorial TEXT,
        paginas INTEGER
        )'''
        c.execute(sql)
        coneccion.commit()

    def create_database_autores(self, coneccion):
        c = coneccion.cursor()
        sql = '''CREATE TABLE IF NOT EXISTS autores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL
        )'''
        c.execute(sql)
        coneccion.commit()

    def create_database_escribe(self, coneccion):
        c = coneccion.cursor()
        sql = '''CREATE TABLE IF NOT EXISTS escribe (
        id integer PRIMARY KEY AUTOINCREMENT,
        autor_id INTEGER NOT NULL,
        libro_id INTEGER NOT NULL,
        FOREIGN KEY(autor_id) REFERENCES autores(id) ON UPDATE SET NULL ON DELETE SET NULL,
        FOREIGN KEY(libro_id) REFERENCES libros(id) ON UPDATE SET NULL ON DELETE SET NULL
        )'''
        c.execute(sql)
        coneccion.commit()

    def create_database_ejemplares(self, coneccion):
        c = coneccion.cursor()
        sql = '''CREATE TABLE IF NOT EXISTS ejemplares (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        localizacion TEXT NOT NULL,
        libro_id INTEGER NOT NULL,
        FOREIGN KEY(libro_id) REFERENCES libros(id) ON UPDATE SET NULL ON DELETE SET NULL
        )'''
        c.execute(sql)
        coneccion.commit()

    def create_database_saca(self, coneccion):
        c = coneccion.cursor()
        sql = '''CREATE TABLE IF NOT EXISTS saca (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha_prestamo DATE NOT NULL,
        fecha_devolucion DATE NOT NULL,
        alumno_id INTEGER,
        ejemplar_id INTEGER,
        FOREIGN KEY(alumno_id) REFERENCES alumnos(id) ON UPDATE SET NULL ON DELETE SET NULL,
        FOREIGN KEY(ejemplar_id) REFERENCES ejemplares(id) ON UPDATE SET NULL ON DELETE SET NULL
        )'''
        c.execute(sql)
        coneccion.commit()

    def clear_database(coneccion, table_name):
        c = coneccion.cursor()
        sql = 'drop table ' + table_name
        c.execute(sql)
        coneccion.commit()

    def mostrar_datos(self, tabla, campo='*'):
        coneccion = self.coneccion.cursor()
        #coneccion.row_factory = sqlite3.Row
        request = f'''SELECT {campo} FROM {tabla}'''
        coneccion.execute(request)
        datos = coneccion.fetchall()
        columns = [n for n, *_ in coneccion.description]
        coneccion.close()
        return datos, columns
    
    def elimina_datos(self, tabla, id):
        coneccion = self.coneccion.cursor()
        print(f"Eliminado de la tabla {tabla} el id {id}")
        request = f'''DELETE FROM {tabla} WHERE id = {id} '''
        coneccion.execute(request)
        self.coneccion.commit()
        coneccion.close()

    def mostrar_datos_by_id(self, tabla, id, campo='*'):
        coneccion = self.coneccion.cursor()
        #coneccion.row_factory = sqlite3.Row
        request = f'''SELECT {campo} FROM {tabla} WHERE id={id}'''
        coneccion.execute(request)
        datos = coneccion.fetchone()
        coneccion.close()
        if datos and campo=='*':
            return datos
        elif datos:
            return datos.get(campo)
        return 'NO data'


    # DATOS ALUMNOS
    def inserta_datos_alumnos(self, tabla, nombre, telefono, direccion):
        coneccion = self.coneccion.cursor()
        print(f"Insertamos datos de la tabla {tabla} el dato {nombre}")
        request = f'''INSERT INTO {tabla} (nombre, telefono, direccion) VALUES ('{nombre}','{telefono}','{direccion}')'''
        coneccion.execute(request)
        self.coneccion.commit()
        coneccion.close()

    def actualiza_datos_alumnos(self, tabla, nombre, telefono, direccion, id):
        coneccion = self.coneccion.cursor()
        print(f"Actualizamos datos de la tabla {tabla} el dato {id} {nombre} {telefono} {direccion}")
        request = f'''UPDATE '{tabla}' SET 'nombre'='{nombre}', 'telefono'='{telefono}', 'direccion'='{direccion}' WHERE id={id} '''
        coneccion.execute(request)
        self.coneccion.commit()
        coneccion.close()

    # DATOS ESCRITORES
    def inserta_datos_escritores(self, tabla, nombre):
        coneccion = self.coneccion.cursor()
        print(f"Insertamos datos de la tabla {tabla} el dato {nombre}")
        request = f'''INSERT INTO {tabla} (nombre) VALUES ('{nombre}')'''
        coneccion.execute(request)
        self.coneccion.commit()
        coneccion.close()

    def actualiza_datos_escritores(self, tabla, nombre, id):
        coneccion = self.coneccion.cursor()
        print(f"Actualizamos datos de la tabla {tabla} el dato {id}")
        request = f'''UPDATE '{tabla}' SET 'nombre'='{nombre}' WHERE id={id} '''
        coneccion.execute(request)
        self.coneccion.commit()
        coneccion.close()

    # DATOS LIBROS
    def inserta_datos_libro(self, tabla, titulo, isbn, editorial, paginas):
        coneccion = self.coneccion.cursor()
        print(f"Insertamos datos de la tabla {tabla} el dato {titulo}")
        request = f'''INSERT INTO {tabla} (titulo, isbn, editorial, paginas) VALUES ('{titulo}','{isbn}','{editorial}','{paginas}')'''
        coneccion.execute(request)
        self.coneccion.commit()
        coneccion.close()

    def actualiza_datos_libro(self, tabla, titulo, isbn, editorial, paginas, id):
        coneccion = self.coneccion.cursor()
        print(f"Actualizamos datos de la tabla {tabla} el dato {id}")
        request = f'''UPDATE '{tabla}' SET 'titulo'='{titulo}', 'isbn'='{isbn}', 'editorial'='{editorial}', 'paginas'='{paginas}' WHERE id={id} '''
        coneccion.execute(request)
        self.coneccion.commit()
        coneccion.close()

    # DATOS ESCRIBE
    def inserta_datos_escribe(self, tabla, autor_id, libro_id):
        coneccion = self.coneccion.cursor()
        print(f"Insertamos datos de la tabla {tabla} el id {autor_id} autor {autor_id} libro {libro_id}")
        request = f'''INSERT INTO '{tabla}' (autor_id, libro_id) VALUES ({autor_id},{libro_id})'''
        coneccion.execute(request)
        self.coneccion.commit()
        coneccion.close()

    # DATOS EJEMPLARES
    def inserta_datos_ejemplares(self, tabla, localizacion, libro_id):
        coneccion = self.coneccion.cursor()

        print(f"Insertamos datos de la tabla {tabla} el id {localizacion} localizacion {localizacion} libro {libro_id}")
        request = f'''INSERT INTO '{tabla}' (localizacion, libro_id) VALUES ('{localizacion}',{libro_id})'''
        coneccion.execute(request)
        self.coneccion.commit()
        coneccion.close()

    # DATOS SACA
    def inserta_datos_saca(self, tabla, fecha_prestamo, fecha_devolucion, alumno_id, ejemplar_id):
        coneccion = self.coneccion.cursor()

        print(f"Insertamos datos de la tabla {tabla} el fecha prestamo {fecha_prestamo} fecha devolucion {fecha_devolucion} libro {ejemplar_id} Alumno {alumno_id}")
        request = f'''INSERT INTO '{tabla}' (fecha_prestamo, fecha_devolucion, alumno_id, ejemplar_id) VALUES ('{fecha_prestamo}','{fecha_devolucion}','{alumno_id}',{ejemplar_id})'''
        coneccion.execute(request)
        self.coneccion.commit()
        coneccion.close()


    def mostrar_usuarios_by_libros(self, tabla, usuario, campo='*'):
        coneccion = self.coneccion.cursor()
        request = f'''
        SELECT {campo} FROM {tabla} 
        INNER JOIN 
        WHERE id={id}

        '''
        coneccion.execute(request)
        datos = coneccion.fetchone()
        coneccion.close()
        if datos:
            return datos.get(campo)
        return 'NO data'
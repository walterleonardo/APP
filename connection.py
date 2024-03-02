import sqlite3


class Coneccion():
    def __init__(self) -> None:
        self.coneccion = sqlite3.connect('./db.sqlite3')
        # Convertir resultado en diccionario
        def row_to_dict(cursor: sqlite3.Cursor, row: sqlite3.Row) -> dict:
            data = {}
            for idx, col in enumerate(cursor.description):
                data[col[0]] = row[idx]
            return data
        self.coneccion.row_factory = row_to_dict

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


    
    # # DATOS ESPECIFICOS
    # def inserta_datos(self, tabla, nombre, telefono, direccion):
    #     coneccion = self.coneccion.cursor()
    #     print(f"Insertamos datos de la tabla {tabla} el dato {nombre}")
    #     request = f'''INSERT INTO {tabla} (Nombre, Telefono, Direccion) VALUES ('{nombre}','{telefono}','{direccion}')'''
    #     coneccion.execute(request)
    #     self.coneccion.commit()
    #     coneccion.close()

    # def actualiza_datos(self, tabla, nombre, telefono, direccion, id):
    #     coneccion = self.coneccion.cursor()
    #     print(f"Actualizamos datos de la tabla {tabla} el dato {id}")
    #     request = f'''UPDATE '{tabla}' SET 'Nombre'='{nombre}', 'Telefono'='{telefono}', 'Direccion'='{direccion}' WHERE id={id} '''
    #     coneccion.execute(request)
    #     self.coneccion.commit()
    #     coneccion.close()

    # DATOS ALUMNOS
    def inserta_datos_alumnos(self, tabla, nombre, telefono, direccion):
        coneccion = self.coneccion.cursor()
        print(f"Insertamos datos de la tabla {tabla} el dato {nombre}")
        request = f'''INSERT INTO {tabla} (Nombre, Telefono, Direccion) VALUES ('{nombre}','{telefono}','{direccion}')'''
        coneccion.execute(request)
        self.coneccion.commit()
        coneccion.close()

    def actualiza_datos_alumnos(self, tabla, nombre, telefono, direccion, id):
        coneccion = self.coneccion.cursor()
        print(f"Actualizamos datos de la tabla {tabla} el dato {id}")
        request = f'''UPDATE '{tabla}' SET 'Nombre'='{nombre}', 'Telefono'='{telefono}', 'Direccion'='{direccion}' WHERE id={id} '''
        coneccion.execute(request)
        self.coneccion.commit()
        coneccion.close()

    # DATOS ESCRITORES
    def inserta_datos_escritores(self, tabla, nombre):
        coneccion = self.coneccion.cursor()
        print(f"Insertamos datos de la tabla {tabla} el dato {nombre}")
        request = f'''INSERT INTO {tabla} (Nombre) VALUES ('{nombre}')'''
        coneccion.execute(request)
        self.coneccion.commit()
        coneccion.close()

    def actualiza_datos_escritores(self, tabla, nombre, id):
        coneccion = self.coneccion.cursor()
        print(f"Actualizamos datos de la tabla {tabla} el dato {id}")
        request = f'''UPDATE '{tabla}' SET 'Nombre'='{nombre}' WHERE id={id} '''
        coneccion.execute(request)
        self.coneccion.commit()
        coneccion.close()

    # DATOS LIBROS
    def inserta_datos_libro(self, tabla, titulo, isbn, editorial, paginas):
        coneccion = self.coneccion.cursor()
        print(f"Insertamos datos de la tabla {tabla} el dato {titulo}")
        request = f'''INSERT INTO {tabla} (Titulo, ISBN, Editorial, Paginas) VALUES ('{titulo}','{isbn}','{editorial}','{paginas}')'''
        coneccion.execute(request)
        self.coneccion.commit()
        coneccion.close()

    def actualiza_datos_libro(self, tabla, titulo, isbn, editorial, paginas, id):
        coneccion = self.coneccion.cursor()
        print(f"Actualizamos datos de la tabla {tabla} el dato {id}")
        request = f'''UPDATE '{tabla}' SET 'Titulo'='{titulo}', 'ISBN'='{isbn}', 'Editorial'='{editorial}', 'Paginas'='{paginas}' WHERE id={id} '''
        coneccion.execute(request)
        self.coneccion.commit()
        coneccion.close()

    # DATOS ESCRIBE
    def inserta_datos_escribe(self, tabla, autorid_id, libroid_id):
        coneccion = self.coneccion.cursor()
        print(f"Insertamos datos de la tabla {tabla} el id {autorid_id} autor {autorid_id} libro {libroid_id}")
        request = f'''INSERT INTO '{tabla}' (AutorId_Id, LibroId_Id) VALUES ({autorid_id},{libroid_id})'''
        print(request)
        coneccion.execute(request)
        self.coneccion.commit()
        coneccion.close()

    # DATOS EJEMPLARES
    def inserta_datos_ejemplares(self, tabla, localizacion, libroid_id):
        coneccion = self.coneccion.cursor()

        print(f"Insertamos datos de la tabla {tabla} el id {localizacion} localizacion {localizacion} libro {libroid_id}")
        request = f'''INSERT INTO '{tabla}' (Localizacion, LibroId_Id) VALUES ('{localizacion}',{libroid_id})'''
        print(request)
        coneccion.execute(request)
        self.coneccion.commit()
        coneccion.close()

    # DATOS SACA
    def inserta_datos_saca(self, tabla, fecha_prestamo, fecha_devolucion, alumno_id, ejemplar_id):
        coneccion = self.coneccion.cursor()

        print(f"Insertamos datos de la tabla {tabla} el fecha prestamo {fecha_prestamo} fecha devolucion {fecha_devolucion} libro {ejemplar_id} Alumno {alumno_id}")
        request = f'''INSERT INTO '{tabla}' (FechaPrestamo, FechaDevolucion, AlumnoId_Id, EjemplarId_Id) VALUES ('{fecha_prestamo}','{fecha_devolucion}','{alumno_id}',{ejemplar_id})'''
        print(request)
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
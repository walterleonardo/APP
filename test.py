'''
TABLA Usuarios, con columnas como id, Nombre y Edad
TABLA Address, con coplumnas como id, id_usuario (foreinKey de Usuarios id), y otra columna con Pais
'''

import sqlite3


db = "./DBUsuarios.db"

###  Select Normal
connection = sqlite3.connect(db)
current_connection = connection.cursor()
request = """
SELECT *
FROM Usuarios
"""
current_connection.execute(request)
data = current_connection.fetchall()
connection.close()
print("La data cruda como la recive")
print(data)
print("Destripamos los datos con un for")

for x in data:
    print(x[1],x[2])






### Select con INNER JOIN junta todas las tablas en una sola. 
# connection = sqlite3.connect(db)
# current_connection = connection.cursor()
# request = """
# SELECT Nombre
# FROM Usuarios
# INNER JOIN Address on Address.id_usuario = Usuarios.id
# WHERE pais = 'España'
# """
# current_connection.execute(request)
# data = current_connection.fetchall()
# connection.close()
# print(data)


## INSERT con valores
connection = sqlite3.connect(db)
current_connection = connection.cursor()
request = """
INSERT INTO Usuarios ('Nombre', 'Edad') VALUES ('Joseee', 22);
"""
connection.execute(request)
connection.commit()
connection.close()


###  Select pidiendo el ID de un usuario
# connection = sqlite3.connect(db)
# current_connection = connection.cursor()
# request = """
# SELECT id
# FROM Usuarios
# WHERE Nombre = 'Joseee'
# """
# current_connection.execute(request)
# data = current_connection.fetchall()
# connection.close()
# print("La data cruda como la recive")
# print(data)
# print("buscamos la info del primer grupo su primer valor")
# print(data[0][0])

### UPDATE con valores
# connection = sqlite3.connect(db)
# current_connection = connection.cursor()
# request = """
# UPDATE Usuarios
# SET Nombre = 'jooose',
#     Edad = '33'
# WHERE
#     id = 4
# """
# current_connection.execute(request)
# connection.commit()
# connection.close()


# ## DELETE con ID
# connection = sqlite3.connect(db)
# current_connection = connection.cursor()
# request = """
# DELETE FROM Usuarios
# WHERE Nombre = 'Joseee'
# """
# current_connection.execute(request)
# connection.commit()
# connection.close()
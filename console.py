from connection import Coneccion
import sys
from os import system


def Menu(menu):
    """
    Aparece un menu, con los nombres de las funciones
    """
    for k, function in menu.items():
        print(k, function.__name__)


def alumnos():
    print("Has seleccionado la opcion alumnos")
    table_name = 'alumnos'
    con = Coneccion()
    rows, columns = con.mostrar_datos(table_name)
    for x in rows:
        print(x)
    value_input = input("Presiona ENTER para continuar, o 1 para borrar, o 2 para insertar\n")
    if (value_input == '1'):
        id = int(input("Dame el ID para borrar\n"))
        con.elimina_datos(table_name, id)
        print(f'Alumno con ID {id} fue eliminado\n')
    if (value_input == '2'):
        datos = input("Dame el nombre, telefono y direccion, separado por comas\n")
        datos_list = datos.split(',')
        if len(datos_list) == 3:
            con.inserta_datos_alumnos('alumnos', datos_list[0], datos_list[1], datos_list[2])
            print(f'Alumno agregado...\n')
        else:
            print("Necesito los datos correctos")
    print("############")
    #system('clear')  # Limpia


def autores():
    print("Has seleccionado la opcion autores")
    table_name = 'autores'
    con = Coneccion()
    rows, columns = con.mostrar_datos(table_name)
    for x in rows:
        print(x)
    value_input = input("Presiona ENTER para continuar, o 1 para borrar, o 2 para insertar\n")
    if (value_input == '1'):
        id = int(input("Dame el ID para borrar\n"))
        con.elimina_datos(table_name, id)
        print(f'Autpr con ID {id} fue eliminado\n')
    if (value_input == '2'):
        datos = input("Dame el nombre\n")
        if datos:
            con.inserta_datos_escritores('autores', datos)
            print(f'Escritor agregado...\n')
        else:
            print("Necesito los datos correctos")
    print("############")
    #system('clear')  # Limpia


def libros():
    print("Has seleccionado la opcion libros") 
    table_name = 'libros'
    con = Coneccion()
    rows, columns = con.mostrar_datos(table_name)
    for x in rows:
        print(x)
    value_input = input("Presiona ENTER para continuar, o 1 para borrar, o 2 para insertar\n")
    if (value_input == '1'):
        id = int(input("Dame el ID para borrar\n"))
        con.elimina_datos(table_name, id)
        print(f'Libro con ID {id} fue eliminado\n')
    if (value_input == '2'):
        datos = input("Dame el titulo, isbn, editorial y paginas, separado por comas\n")
        datos_list = datos.split(',')
        if len(datos_list) == 4:
            con.inserta_datos_libro('libros', datos_list[0], datos_list[1], datos_list[2], datos_list[3])
            print(f'Libro agregado...\n')
        else:
            print("Necesito los datos correctos")
    print("############")
    #system('clear')  # Limpia

def escribe():
    print("Has seleccionado la opcion libros") 
    table_name = 'escribe'
    con = Coneccion()
    print("## autores")
    rows, columns = con.mostrar_datos("autores")
    for x in rows:
        print(x)
    print("## libros")
    rows, columns = con.mostrar_datos("libros")
    for x in rows:
        print(x)
    print("###################################")
    rows, columns = con.mostrar_datos(table_name)
    for x in rows:
        print(x)
    value_input = input("Presiona ENTER para continuar, o 1 para borrar, o 2 para insertar\n")
    if (value_input == '1'):
        id = int(input("Dame el ID para borrar\n"))
        con.elimina_datos(table_name, id)
        print(f'Libro con ID {id} fue eliminado\n')
    if (value_input == '2'):
        datos = input("Dame el AutorID y el LibroID, separado por comas\n")
        datos_list = datos.split(',')
        if len(datos_list) == 2:
            con.inserta_datos_escribe('escribe', datos_list[0], datos_list[1])
            print(f'Escribe agregado...\n')
        else:
            print("Necesito los datos correctos")
    print("############")
    #system('clear')  # Limpia

def ejemplares():
    print("Has seleccionado la opcion Ejemplar") 
    table_name = 'ejemplares'
    con = Coneccion()
    print("## libros")
    rows, columns = con.mostrar_datos("libros")
    for x in rows:
        print(x)
    print("###################################")
    rows, columns = con.mostrar_datos(table_name)
    for x in rows:
        print(x)
    value_input = input("Presiona ENTER para continuar, o 1 para borrar, o 2 para insertar\n")
    if (value_input == '1'):
        id = int(input("Dame el ID para borrar\n"))
        con.elimina_datos(table_name, id)
        print(f'Libro con ID {id} fue eliminado\n')
    if (value_input == '2'):
        datos = input("Dame el Localizacion y el LibroID, separado por comas\n")
        datos_list = datos.split(',')
        if len(datos_list) == 2:
            con.inserta_datos_ejemplares('ejemplares', datos_list[0], datos_list[1])
            print(f'Alumno agregado...\n')
        else:
            print("Necesito los datos correctos")
    print("############")
    #system('clear')  # Limpia

def saca():
    print("Has seleccionado la opcion Ejemplar") 
    table_name = 'saca'
    con = Coneccion()
    print("## Ejemplar")
    rows, columns = con.mostrar_datos("ejemplares")
    for x in rows:
        print(x)
    print("###################################")
    print("## alumnos")
    rows, columns = con.mostrar_datos("alumnos")
    for x in rows:
        print(x)
    print("###################################")
    rows, columns = con.mostrar_datos(table_name)
    for x in rows:
        print(x)
    value_input = input("Presiona ENTER para continuar, o 1 para borrar, o 2 para insertar\n")
    if (value_input == '1'):
        id = int(input("Dame el ID para borrar\n"))
        con.elimina_datos(table_name, id)
        print(f'Libro con ID {id} fue eliminado\n')
    if (value_input == '2'):
        datos = input("Dame el EjemplarID y el AlumnoID, Fecha de salida y fecha de entrada, separado por comas\n")
        datos_list = datos.split(',')
        if len(datos_list) == 4:
            con.inserta_datos_saca('ejemplares', datos_list[0], datos_list[1], datos_list[2], datos_list[3])
            print(f'Alumno agregado...\n')
        else:
            print("Necesito los datos correctos")
    print("############")
    #system('clear')  # Limpia


def Salir():
    system('clear')  # Limpia
    print("Goodbye")
    sys.exit()


def main():
    functions_names = [alumnos, autores, libros, escribe, ejemplares, saca, Salir]
    menu_items = dict(enumerate(functions_names, start=1))

    while True:
        Menu(menu_items)
        print("####################")
        try:
            selection = int(input("Entre la opcion deseada: ")) # Espera la funcion
        except:
            selection = 0
        if selection != 0:
            selected_value = menu_items[selection]  # Obtiene las funciones
            selected_value()  # Llama a la funcion


if __name__ == "__main__":
    main()
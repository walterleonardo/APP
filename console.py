from connection import Coneccion
import sys
from os import system


def Menu(menu):
    """
    Aparece un menu, con los nombres de las funciones
    """
    for k, function in menu.items():
        print(k, function.__name__)


def Alumnos():
    print("Has seleccionado la opcion Alumnos")
    table_name = 'Alumnos'
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
            con.inserta_datos('Alumnos', datos_list[0], datos_list[1], datos_list[2])
            print(f'Alumno agregado...\n')
        else:
            print("Necesito los datos correctos")
    print("############")
    #system('clear')  # Limpia


def Autores():
    print("Has seleccionado la opcion Autores")
    table_name = 'Autores'
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
            con.inserta_datos('Autores', datos)
            print(f'Autor agregado...\n')
        else:
            print("Necesito los datos correctos")
    print("############")
    #system('clear')  # Limpia


def Libros():
    print("Has seleccionado la opcion Libros") 
    table_name = 'Libros'
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
            con.inserta_datos('Libros', datos_list[0], datos_list[1], datos_list[2], datos_list[3])
            print(f'Alumno agregado...\n')
        else:
            print("Necesito los datos correctos")
    print("############")
    #system('clear')  # Limpia

def Escribe():
    print("Has seleccionado la opcion Libros") 
    table_name = 'Escribe'
    con = Coneccion()
    print("## Autores")
    rows, columns = con.mostrar_datos("Autores")
    for x in rows:
        print(x)
    print("## Libros")
    rows, columns = con.mostrar_datos("Libros")
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
            con.inserta_datos('Escribe', datos_list[0], datos_list[1])
            print(f'Alumno agregado...\n')
        else:
            print("Necesito los datos correctos")
    print("############")
    #system('clear')  # Limpia

def Ejemplares():
    print("Has seleccionado la opcion Ejemplar") 
    table_name = 'Ejemplares'
    con = Coneccion()
    print("## Libros")
    rows, columns = con.mostrar_datos("Libros")
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
            con.inserta_datos('Ejemplares', datos_list[0], datos_list[1])
            print(f'Alumno agregado...\n')
        else:
            print("Necesito los datos correctos")
    print("############")
    #system('clear')  # Limpia

def Saca():
    print("Has seleccionado la opcion Ejemplar") 
    table_name = 'Saca'
    con = Coneccion()
    print("## Ejemplar")
    rows, columns = con.mostrar_datos("Ejemplares")
    for x in rows:
        print(x)
    print("###################################")
    print("## Alumnos")
    rows, columns = con.mostrar_datos("Alumnos")
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
            con.inserta_datos('Ejemplares', datos_list[0], datos_list[1], datos_list[2], datos_list[3])
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
    functions_names = [Alumnos, Autores, Libros, Escribe, Ejemplares, Saca, Salir]
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
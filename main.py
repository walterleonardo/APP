#!/usr/bin/env python3
from nicegui import app, ui, events
import time
from tortoise import Tortoise
from typing import List
import sqlite3
import models
import json
from connection import Coneccion
# Alumnos = ''
# async def init_db() -> None:
#     await Tortoise.init(db_url='sqlite://db.sqlite3', modules={'models': ['models']})
#     await Tortoise.generate_schemas()


# async def close_db() -> None:
#     await Tortoise.close_connections()

# app.on_startup(init_db)
# app.on_shutdown(close_db)



def table_alumnos(ui):
    table_name = 'alumnos'
    con = Coneccion()
    rows, columns = con.mostrar_datos(table_name)

    columns_name = []
    for x in columns:
        if x == 'id': continue
        columns_name.append({'name': x, 'label': x, 'field': x, 'required': True})
    
    
    table = ui.table(columns=columns_name, rows=rows, row_key='id').classes('w-260')

    def add_row() -> None:
        if not rows:
            new_id = 1
        else:
            new_id = max(dx['id'] for dx in rows) + 1
        rows.append({'id': new_id, 'Nombre': 'Nombre', 'Telefono': 917, 'Direccion': 'Direccion'})
        ui.notify(f'Added new row with ID {new_id}')
        con.inserta_datos_alumnos(table_name,'Nombre', 917, 'Direccion')
        table.update()


    def rename(e: events.GenericEventArguments) -> None:
        for row in rows:
            if row['id'] == e.args['id']:
                row.update(e.args)
        ui.notify(f'Updated rows to: {table.rows}')
        con.actualiza_datos_alumnos(table_name, e.args['Nombre'], e.args['Telefono'], e.args['Direccion'], e.args['id'])
        table.update()


    def delete(e: events.GenericEventArguments) -> None:
        rows[:] = [row for row in rows if row['id'] != e.args['id']]
        ui.notify(f'Deleted row with ID {e.args["id"]}')
        con.elimina_datos(table_name, e.args["id"])
        table.update()


    table.add_slot('header', r'''
        <q-tr :props="props">
            <q-th auto-width />
            <q-th v-for="col in props.cols" :key="col.name" :props="props">
                {{ col.label }}
            </q-th>
        </q-tr>
    ''')
    table.add_slot('body', r'''
            <q-tr :props="props">
                <q-td auto-width >
                    <q-btn size="sm" color="warning" round dense icon="delete"
                        @click="() => $parent.$emit('delete', props.row)"
                    />
                </q-td>
                       
                <q-td key="Nombre" :props="props">
                    {{ props.row.Nombre }}
                    <q-popup-edit v-model="props.row.Nombre" v-slot="scope"
                        @update:model-value="() => $parent.$emit('rename', props.row)"
                    >
                        <q-input v-model="scope.value" dense autofocus counter @keyup.enter="scope.set" />
                    </q-popup-edit>
                </q-td>
                <q-td key="Telefono" :props="props">
                    {{ props.row.Telefono }}
                    <q-popup-edit v-model="props.row.Telefono" v-slot="scope" 
                        @update:model-value="() => $parent.$emit('rename', props.row)"
                    >
                        <q-input v-model.number="scope.value" type="number" dense autofocus counter @keyup.enter="scope.set" />
                    </q-popup-edit>
                </q-td>
                       <q-td key="Direccion" :props="props">
                    {{ props.row.Direccion }}
                    <q-popup-edit v-model="props.row.Direccion" v-slot="scope" 
                        @update:model-value="() => $parent.$emit('rename', props.row)"
                    >
                        <q-input v-model.number="scope.value" type="number" dense autofocus counter @keyup.enter="scope.set" />
                    </q-popup-edit>
                </q-td>
            </q-tr>
        ''')
    with table.add_slot('bottom-row'):
        with table.cell().props('colspan=4'):
            ui.button('Add row', icon='add', color='accent', on_click=add_row).classes('w-full')
    table.on('rename', rename)
    table.on('delete', delete)

def table_libros(ui):
        table_name = 'libros'
        con = Coneccion()
        rows, columns = con.mostrar_datos(table_name)

        columns_name = []
        for x in columns:
            if x == 'id': continue
            columns_name.append({'name': x, 'label': x, 'field': x, 'required': False})

        table = ui.table(columns=columns_name, rows=rows, row_key='id').classes('w-260')
        def add_row() -> None:
            if not rows:
                new_id = 1
            else:
                new_id = max(dx['id'] for dx in rows) + 1
            rows.append({'id': new_id, 'Titulo': 'Titulo', 'ISBN': 000, 'Editorial': 'Editorial', 'Paginas': 10})
            ui.notify(f'Added in table {table_name} new row with ID {new_id}')
            con.inserta_datos_libro(table_name,'Titulo', 000, 'Editorial', 10)
            table.update()


        def rename(e: events.GenericEventArguments) -> None:
            for row in rows:
                if row['id'] == e.args['id']:
                    row.update(e.args)
            ui.notify(f'Updated rows to: {table.rows}')
            con.actualiza_datos_libro(table_name, e.args['Titulo'], e.args['ISBN'], e.args['Editorial'], e.args['Paginas'], e.args['id'])
            table.update()


        def delete(e: events.GenericEventArguments) -> None:
            rows[:] = [row for row in rows if row['id'] != e.args['id']]
            ui.notify(f'Deleted row with ID {e.args["id"]}')
            con.elimina_datos(table_name, e.args["id"])
            table.update()


        table.add_slot('header', r'''
            <q-tr :props="props">
                <q-th auto-width />
                <q-th v-for="col in props.cols" :key="col.name" :props="props">
                    {{ col.label }}
                </q-th>
            </q-tr>
        ''')
        table.add_slot('body', r'''
            <q-tr :props="props">
                <q-td auto-width >
                    <q-btn size="sm" color="warning" round dense icon="delete"
                        @click="() => $parent.$emit('delete', props.row)"
                    />
                </q-td>
                       
                <q-td key="Titulo" :props="props">
                    {{ props.row.Titulo }}
                    <q-popup-edit v-model="props.row.Titulo" v-slot="scope"
                        @update:model-value="() => $parent.$emit('rename', props.row)"
                    >
                        <q-input v-model="scope.value" dense autofocus counter @keyup.enter="scope.set" />
                    </q-popup-edit>
                </q-td>
                <q-td key="ISBN" :props="props">
                    {{ props.row.ISBN }}
                    <q-popup-edit v-model="props.row.ISBN" v-slot="scope" 
                        @update:model-value="() => $parent.$emit('rename', props.row)"
                    >
                        <q-input v-model.number="scope.value" type="number" dense autofocus counter @keyup.enter="scope.set" />
                    </q-popup-edit>
                </q-td>
                <q-td key="Editorial" :props="props">
                    {{ props.row.Editorial }}
                    <q-popup-edit v-model="props.row.Editorial" v-slot="scope" 
                        @update:model-value="() => $parent.$emit('rename', props.row)"
                    >
                        <q-input v-model.number="scope.value" type="number" dense autofocus counter @keyup.enter="scope.set" />
                    </q-popup-edit>
                </q-td>
                <q-td key="Paginas" :props="props">
                    {{ props.row.Paginas }}
                    <q-popup-edit v-model="props.row.Paginas" v-slot="scope" 
                        @update:model-value="() => $parent.$emit('rename', props.row)"
                    >
                        <q-input v-model.number="scope.value" type="number" dense autofocus counter @keyup.enter="scope.set" />
                    </q-popup-edit>
                </q-td>
            </q-tr>
        ''')
        with table.add_slot('bottom-row'):
            with table.cell().props('colspan=4'):
                ui.button('Add row', icon='add', color='accent', on_click=add_row).classes('w-full')
        table.on('rename', rename)
        table.on('delete', delete)

def table_escritores(ui):
        table_name = 'Autores'
        con = Coneccion()
        rows, columns = con.mostrar_datos(table_name)

        columns_name = []
        for x in columns:
            if x == 'id': continue
            columns_name.append({'name': x, 'label': x, 'field': x, 'required': True})
        
        table = ui.table(columns=columns_name, rows=rows, row_key='id').classes('w-260')
        def add_row() -> None:
            if not rows:
                new_id = 1
            else:
                new_id = max(dx['id'] for dx in rows) + 1
            rows.append({'id': new_id, 'Nombre': 'Nombre'})
            ui.notify(f'Added new row with ID {new_id}')
            con.inserta_datos_escritores(table_name,'Nombre')
            table.update()


        def rename(e: events.GenericEventArguments) -> None:
            for row in rows:
                if row['id'] == e.args['id']:
                    row.update(e.args)
            ui.notify(f'Updated rows to: {table.rows}')
            con.actualiza_datos_escritores(table_name, e.args['Nombre'], e.args['id'])
            table.update()


        def delete(e: events.GenericEventArguments) -> None:
            rows[:] = [row for row in rows if row['id'] != e.args['id']]
            ui.notify(f'Deleted row with ID {e.args["id"]}')
            con.elimina_datos(table_name, e.args["id"])
            table.update()


        table.add_slot('header', r'''
            <q-tr :props="props">
                <q-th auto-width />
                <q-th v-for="col in props.cols" :key="col.name" :props="props">
                    {{ col.label }}
                </q-th>
            </q-tr>
        ''')
        
        table.add_slot('body', r'''
            <q-tr :props="props">
                <q-td auto-width >
                    <q-btn size="sm" color="warning" round dense icon="delete"
                        @click="() => $parent.$emit('delete', props.row)"
                    />
                </q-td>
                       
                <q-td key="Nombre" :props="props">
                    {{ props.row.Nombre }}
                    <q-popup-edit v-model="props.row.Nombre" v-slot="scope"
                        @update:model-value="() => $parent.$emit('rename', props.row)"
                    >
                        <q-input v-model="scope.value" dense autofocus counter @keyup.enter="scope.set" />
                    </q-popup-edit>
                </q-td>
            </q-tr>
        ''')
        with table.add_slot('bottom-row'):
            with table.cell().props('colspan=4'):
                ui.button('Add row', icon='add', color='accent', on_click=add_row).classes('w-full')
        table.on('rename', rename)
        table.on('delete', delete)



def table_escribe(ui):
        table_name = 'escribe'
        con = Coneccion()
        rows, columns = con.mostrar_datos(table_name)

        columns_name = []
        for x in columns:
            if x == 'id': continue
            columns_name.append({'name': x, 'label': x, 'field': x, 'required': True})


        for x in rows:
            nombre = (con.mostrar_datos_by_id('autores', x.get('AutorId_id'), 'Nombre'))
            x['AutorId_id'] = nombre
            libro = (con.mostrar_datos_by_id('libros', x.get('LibroId_id'), 'Titulo'))
            x['LibroId_id'] = libro

        table = ui.table(columns=columns_name, rows=rows, row_key='id').classes('w-260')
        
        def add_row() -> None:

            if not select1.value or not select2.value:
                ui.notify(f'Faltan datos!!!')
                return False

            if not rows:
                new_id = 1
            else:
                new_id = max(dx['id'] for dx in rows) + 1
            autor = (con.mostrar_datos_by_id('autores', select1.value, 'Nombre'))
            libro = (con.mostrar_datos_by_id('libros', select2.value, 'Titulo'))

            rows.append({'id': new_id, 'AutorId_id': autor, 'LibroId_id': libro})
            ui.notify(f'Added in table {table_name} new row with ID {new_id} autor {autor}, libro {libro}')
            con.inserta_datos_escribe(table_name, select1.value, select2.value)
            table.update()


        def delete(e: events.GenericEventArguments) -> None:
            rows[:] = [row for row in rows if row['id'] != e.args['id']]
            ui.notify(f'Deleted row with ID {e.args["id"]}')
            con.elimina_datos(table_name, e.args["id"])
            table.update()


        table.add_slot('header', r'''
            <q-tr :props="props">
                <q-th auto-width />
                <q-th v-for="col in props.cols" :key="col.name" :props="props">
                    {{ col.label }}
                </q-th>
            </q-tr>
        ''')
        table.add_slot('body', r'''
            <q-tr :props="props">
                <q-td auto-width >
                    <q-btn size="sm" color="warning" round dense icon="delete"
                        @click="() => $parent.$emit('delete', props.row)"/>
                </q-td>
                       
                <q-td key="AutorId_id" :props="props">
                    {{ props.row.AutorId_id }}
                </q-td>
                <q-td key="LibroId_id" :props="props">
                    {{ props.row.LibroId_id }}
            </q-tr>
        ''')
        table.on('delete', delete)


        selec_value_libros, columns = con.mostrar_datos('libros', 'id, Titulo')
        selector2_data = {}
        for x in selec_value_libros:
            selector2_data[x.get('id')] = x.get('Titulo') 

        selec_value_autor, columns = con.mostrar_datos('autores', 'id, Nombre')
        selector1_data = {}
        for x in selec_value_autor:
            selector1_data[x.get('id')] = x.get('Nombre') 
        
        with ui.grid(columns=2):
            ui.label('Autor:')
            select1 = ui.select(selector1_data).classes('w-full')
            ui.label('Libro:')
            select2 = ui.select(selector2_data).classes('w-full')
            ui.button('Add row', icon='add', color='accent', on_click=add_row).classes('w-full')


def table_ejemplares(ui):
        table_name = 'ejemplares'
        con = Coneccion()
        rows, columns = con.mostrar_datos(table_name)
        columns_name = []
        for x in columns:
            columns_name.append({'name': x, 'label': x, 'field': x, 'required': True})
        

        for x in rows:
            libro = (con.mostrar_datos_by_id('libros', x.get('LibroId_id'), 'Titulo'))
            x['LibroId_id'] = libro
        table = ui.table(columns=columns_name, rows=rows, row_key='id').classes('w-260')
        print(rows)
        def add_row() -> None:

            if not select1.value or not select2.value:
                ui.notify(f'Faltan datos!!!')
                return False


            if not rows:
                new_id = 1
            else:
                new_id = max(dx['id'] for dx in rows) + 1

            libro = (con.mostrar_datos_by_id('libros', select2.value, 'Titulo'))

            rows.append({'id': new_id, 'Localizacion': select1.value, 'LibroId_id': libro})
            ui.notify(f'Added in table {table_name} new row with ID {new_id} Localizacion {select1.value}, libro {select2.value}')
            con.inserta_datos_ejemplares(table_name, select1.value, select2.value)
            table.update()


        def delete(e: events.GenericEventArguments) -> None:
            rows[:] = [row for row in rows if row['id'] != e.args['id']]
            ui.notify(f'Deleted row with ID {e.args["id"]}')
            con.elimina_datos(table_name, e.args["id"])
            table.update()


        table.add_slot('header', r'''
            <q-tr :props="props">
                <q-th auto-width />
                <q-th v-for="col in props.cols" :key="col.name" :props="props">
                    {{ col.label }}
                </q-th>
            </q-tr>
        ''')
        table.add_slot('body', r'''
            <q-tr :props="props">
                <q-td auto-width >
                    <q-btn size="sm" color="warning" round dense icon="delete"
                        @click="() => $parent.$emit('delete', props.row)"/>
                </q-td>
                                           
                <q-td key="id" :props="props">
                    {{ props.row.id }}
                </q-td>   
                <q-td key="Localizacion" :props="props">
                    {{ props.row.Localizacion }}
                </q-td>
                <q-td key="LibroId_id" :props="props">
                    {{ props.row.LibroId_id }}
            </q-tr>
        ''')
        table.on('delete', delete)


        selec_value_libros, columns = con.mostrar_datos('libros', 'id, Titulo')
        selector2_data = {}
        for x in selec_value_libros:
            selector2_data[x.get('id')] = x.get('Titulo') 



        
        with ui.grid(columns=2):
            select1 = ui.input(label='Localizacion', placeholder='start typing', value='')
            ui.label('Libro:')
            select2 = ui.select(selector2_data).classes('w-full')
            ui.button('Add row', icon='add', color='accent', on_click=add_row).classes('w-full')



def table_saca(ui):
        table_name = 'saca'
        con = Coneccion()
        rows, columns = con.mostrar_datos(table_name)
        columns_name = []
        for x in columns:
            if x == 'id': continue
            columns_name.append({'name': x, 'label': x, 'field': x, 'required': True})
        

        for x in rows:
            libro = (con.mostrar_datos_by_id('libros', x.get('LibroId_id'), 'Titulo'))
            x['LibroId_id'] = libro
            libro = (con.mostrar_datos_by_id('libros', x.get('LibroId_id'), 'Titulo'))
            x['LibroId_id'] = libro
        table = ui.table(columns=columns_name, rows=rows, row_key='id').classes('w-260')
        
        def add_row() -> None:

            if not select1.value or not select2.value:
                ui.notify(f'Faltan datos!!!')
                return False


            if not rows:
                new_id = 1
            else:
                new_id = max(dx['id'] for dx in rows) + 1

            libro = (con.mostrar_datos_by_id('libros', select2.value, 'Titulo'))

            rows.append({'id': new_id, 'Localizacion': select1.value, 'LibroId_id': libro})
            ui.notify(f'Added in table {table_name} new row with ID {new_id} Localizacion {select1.value}, libro {select2.value}')
            con.inserta_datos_ejemplares(table_name, select1.value, select2.value)
            table.update()


        def delete(e: events.GenericEventArguments) -> None:
            rows[:] = [row for row in rows if row['id'] != e.args['id']]
            ui.notify(f'Deleted row with ID {e.args["id"]}')
            con.elimina_datos(table_name, e.args["id"])
            table.update()


        table.add_slot('header', r'''
            <q-tr :props="props">
                <q-th auto-width />
                <q-th v-for="col in props.cols" :key="col.name" :props="props">
                    {{ col.label }}
                </q-th>
            </q-tr>
        ''')
        table.add_slot('body', r'''
            <q-tr :props="props">
                <q-td auto-width >
                    <q-btn size="sm" color="warning" round dense icon="delete"
                        @click="() => $parent.$emit('delete', props.row)"/>
                </q-td>
                       
                <q-td key="Localizacion" :props="props">
                    {{ props.row.Localizacion }}
                </q-td>
                <q-td key="LibroId_id" :props="props">
                    {{ props.row.LibroId_id }}
            </q-tr>
        ''')
        table.on('delete', delete)


        selec_value_libros, columns = con.mostrar_datos('libros', 'id, Titulo')
        selector2_data = {}
        for x in selec_value_libros:
            selector2_data[x.get('id')] = x.get('Titulo') 



        
        with ui.grid(columns=2):
            select1 = ui.input(label='Localizacion', placeholder='start typing', value='')
            ui.label('Libro:')
            select2 = ui.select(selector2_data).classes('w-full')
            ui.button('Add row', icon='add', color='accent', on_click=add_row).classes('w-full')








### NICEGUI ZONE
# Creamos la cabecera. 
with ui.header().classes(replace='row items-center') as header:
    # Formato de tabla
    ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
    # Creamos los tabs superiores
    with ui.tabs() as tabs:
        ui.tab('Alumnos')
        ui.tab('Libros')
        ui.tab('Escritores')
        ui.tab('Escribe')
        ui.tab('Ejemplares')

#Creamos el footer
with ui.footer(value=False) as footer:
    ui.label('Este es el footer y puede incluir info de contacto')

# creamos el panel izquierdo
with ui.left_drawer().classes('bg-green-50') as left_drawer:
    ui.label('Menu')
    with ui.tab_panels(tabs, value='Alumnos').classes('w-full'):
        with ui.tab_panel('Alumnos'):
            ui.label('En este menu puede agregar, borrar o buscar alumnos')
        with ui.tab_panel('Libros'):
            ui.label('En este menu puede agregar, borrar o buscar libros')
        with ui.tab_panel('Escritores'):
            ui.label('En este menu puede agregar, borrar o buscar escritores')
        with ui.tab_panel('Escribe'):
            ui.label('En este menu puede agregar, borrar o buscar escribe')
        with ui.tab_panel('Ejemplares'):
            ui.label('En este menu puede agregar, borrar o buscar ejemplares')
# El footer lo pegamos al fondo
with ui.page_sticky(position='bottom-right', x_offset=10, y_offset=20):
    ui.button(on_click=footer.toggle, icon='contact_support').props('fab')

#Estos son los paneles principales y el value es cual es el default 
with ui.tab_panels(tabs, value='Alumnos').classes('w-full'):
    with ui.tab_panel('Alumnos'):
        # Con la UI creamos una tabla
        table_alumnos(ui)

    with ui.tab_panel('Libros'):
        # Con la UI creamos una tabla
        table_libros(ui)

    with ui.tab_panel('Escritores'):
        # Con la UI creamos una tabla
        table_escritores(ui)

    with ui.tab_panel('Escribe'):
        # Con la UI creamos una tabla
        table_escribe(ui)

    with ui.tab_panel('Ejemplares'):
        # Con la UI creamos una tabla
        table_ejemplares(ui)



# Ejecutamos la UI en el puerto 8888
ui.run(port=8888)

#!/usr/bin/env python3
from nicegui import ui, events
from connection import Coneccion
import socket



def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def table_buscar_escribe(ui):
    con = Coneccion()
    ui.label("Datos de un usuario?")
    usuarios, columnas = con.mostrar_datos('alumnos')
    alumnos_nombre = {}
    for x in usuarios:
        alumnos_nombre[x.get('id')] = x.get('nombre')
    select_alumno = ui.select(
        options=alumnos_nombre, on_change=lambda e: call_db(e.value)).classes('w-full')

    def call_db(value):
        datos = con.mostrar_datos_by_id('alumnos', value)
        ui.label("Estos son los datos")
        ui.label(f'El nombre del usuario es :{datos.get('nombre')}')
        ui.label(f'La direccion del usuario es :{datos.get('direccion')}')
        ui.label(f'El telefono del usuario es :{datos.get('telefono')}')
        ui.label(f'El telefono del usuario es :{datos.get('telefono')}')


def table_alumnos(ui):
    table_name = 'alumnos'
    con = Coneccion()
    rows, columns = con.mostrar_datos(table_name)

    columns_name = []
    for x in columns:
        if x == 'id':
            continue
        columns_name.append(
            {'name': x, 'label': x, 'field': x, 'required': True})
    f = ui.input('Filter')
    table = ui.table(columns=columns_name, rows=rows,
                     row_key='id').classes('w-260').bind_filter_from(f, 'value')

    def add_row() -> None:
        if not rows:
            new_id = 1
        else:
            new_id = max(dx['id'] for dx in rows) + 1
        rows.append({'id': new_id, 'nombre': 'nombre',
                    'telefono': '917', 'direccion': 'direccion'})
        ui.notify(f'Added new row with ID {new_id}')
        con.inserta_datos_alumnos(table_name, 'nombre', '917', 'direccion')
        table.update()

    def rename(e: events.GenericEventArguments) -> None:
        for row in rows:
            if row['id'] == e.args['id']:
                row.update(e.args)

        ui.notify(f'Updated rows to: {table.rows}')
        con.actualiza_datos_alumnos(
            table_name, e.args['nombre'], e.args['telefono'], e.args['direccion'], e.args['id'])
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
                       
                <q-td key="nombre" :props="props">
                    {{ props.row.nombre }}
                    <q-popup-edit v-model="props.row.nombre" v-slot="scope"
                        @update:model-value="() => $parent.$emit('rename', props.row)"
                    >
                        <q-input v-model="scope.value" dense autofocus counter @keyup.enter="scope.set" />
                    </q-popup-edit>
                </q-td>
                <q-td key="telefono" :props="props">
                    {{ props.row.telefono }}
                    <q-popup-edit v-model="props.row.telefono" v-slot="scope" 
                        @update:model-value="() => $parent.$emit('rename', props.row)"
                    >
                        <q-input v-model.number="scope.value" dense autofocus counter @keyup.enter="scope.set" />
                    </q-popup-edit>
                </q-td>
                       <q-td key="direccion" :props="props">
                    {{ props.row.direccion }}
                    <q-popup-edit v-model="props.row.direccion" v-slot="scope" 
                        @update:model-value="() => $parent.$emit('rename', props.row)"
                    >
                        <q-input v-model.number="scope.value" dense autofocus counter @keyup.enter="scope.set" />
                    </q-popup-edit>
                </q-td>
            </q-tr>
        ''')
    with table.add_slot('bottom-row'):
        with table.cell().props('colspan=4'):
            ui.button('Add row', icon='add', color='accent',
                      on_click=add_row).classes('w-full')
    table.on('rename', rename)
    table.on('delete', delete)



def table_libros(ui):
    table_name = 'libros'
    con = Coneccion()
    rows, columns = con.mostrar_datos(table_name)

    columns_name = []
    for x in columns:
        if x == 'id':
            continue
        columns_name.append(
            {'name': x, 'label': x, 'field': x, 'required': False})
    f = ui.input('Filter')
    table = ui.table(columns=columns_name, rows=rows,
                     row_key='id').classes('w-260').bind_filter_from(f, 'value')

    def add_row() -> None:
        if not rows:
            new_id = 1
        else:
            new_id = max(dx['id'] for dx in rows) + 1
        rows.append({'id': new_id, 'titulo': 'titulo', 'isbn': 000,'editorial': 'editorial', 'paginas': 10})
        ui.notify(f'Added in table {table_name} new row with ID {new_id}')
        con.inserta_datos_libro(table_name, 'titulo', 0, 'editorial', 10)
        table.update()

    def rename(e: events.GenericEventArguments) -> None:
        for row in rows:
            if row['id'] == e.args['id']:
                row.update(e.args)
        ui.notify(f'Updated rows to: {table.rows}')
        con.actualiza_datos_libro(
            table_name, e.args['titulo'], e.args['isbn'], e.args['editorial'], e.args['paginas'], e.args['id'])
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
                       
                <q-td key="titulo" :props="props">
                    {{ props.row.titulo }}
                    <q-popup-edit v-model="props.row.titulo" v-slot="scope"
                        @update:model-value="() => $parent.$emit('rename', props.row)"
                    >
                        <q-input v-model="scope.value" dense autofocus counter @keyup.enter="scope.set" />
                    </q-popup-edit>
                </q-td>
                <q-td key="isbn" :props="props">
                    {{ props.row.isbn }}
                    <q-popup-edit v-model="props.row.isbn" v-slot="scope" 
                        @update:model-value="() => $parent.$emit('rename', props.row)"
                    >
                        <q-input v-model.number="scope.value" type="number" dense autofocus counter @keyup.enter="scope.set" />
                    </q-popup-edit>
                </q-td>
                <q-td key="editorial" :props="props">
                    {{ props.row.editorial }}
                    <q-popup-edit v-model="props.row.editorial" v-slot="scope" 
                        @update:model-value="() => $parent.$emit('rename', props.row)"
                    >
                        <q-input v-model.number="scope.value" dense autofocus counter @keyup.enter="scope.set" />
                    </q-popup-edit>
                </q-td>
                <q-td key="paginas" :props="props">
                    {{ props.row.paginas }}
                    <q-popup-edit v-model="props.row.paginas" v-slot="scope" 
                        @update:model-value="() => $parent.$emit('rename', props.row)"
                    >
                        <q-input v-model.number="scope.value" type="number" dense autofocus counter @keyup.enter="scope.set" />
                    </q-popup-edit>
                </q-td>
            </q-tr>
        ''')
    with table.add_slot('bottom-row'):
        with table.cell().props('colspan=4'):
            ui.button('Add row', icon='add', color='accent',
                      on_click=add_row).classes('w-full')
    table.on('rename', rename)
    table.on('delete', delete)


def table_escritores(ui):
    table_name = 'Autores'
    con = Coneccion()
    rows, columns = con.mostrar_datos(table_name)

    columns_name = []
    for x in columns:
        if x == 'id':
            continue
        columns_name.append(
            {'name': x, 'label': x, 'field': x, 'required': True})

    f = ui.input('Filter')
    table = ui.table(columns=columns_name, rows=rows,
                     row_key='id').classes('w-260').bind_filter_from(f, 'value')

    def add_row() -> None:
        if not rows:
            new_id = 1
        else:
            new_id = max(dx['id'] for dx in rows) + 1
        rows.append({'id': new_id, 'nombre': 'nombre'})
        ui.notify(f'Added new row with ID {new_id}')
        con.inserta_datos_escritores(table_name, 'nombre')
        table.update()

    def rename(e: events.GenericEventArguments) -> None:
        for row in rows:
            if row['id'] == e.args['id']:
                row.update(e.args)
        ui.notify(f'Updated rows to: {table.rows}')
        con.actualiza_datos_escritores(
            table_name, e.args['nombre'], e.args['id'])
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
                       
                <q-td key="nombre" :props="props">
                    {{ props.row.nombre }}
                    <q-popup-edit v-model="props.row.nombre" v-slot="scope"
                        @update:model-value="() => $parent.$emit('rename', props.row)"
                    >
                        <q-input v-model="scope.value" dense autofocus counter @keyup.enter="scope.set" />
                    </q-popup-edit>
                </q-td>
            </q-tr>
        ''')
    with table.add_slot('bottom-row'):
        with table.cell().props('colspan=4'):
            ui.button('Add row', icon='add', color='accent',
                      on_click=add_row).classes('w-full')
    table.on('rename', rename)
    table.on('delete', delete)

@ui.refreshable
def table_escribe(ui):
    table_name = 'escribe'
    con = Coneccion()
    rows, columns = con.mostrar_datos(table_name)

    columns_name = []
    for x in columns:
        if x == 'id':
            continue
        columns_name.append(
            {'name': x, 'label': x, 'field': x, 'required': True})

    for x in rows:
        nombre = (con.mostrar_datos_by_id(
            'autores', x.get('autor_id'), 'nombre'))
        x['autor_id'] = nombre
        libro = (con.mostrar_datos_by_id(
            'libros', x.get('libro_id'), 'titulo'))
        x['libro_id'] = libro

    f = ui.input('Filter')
    table = ui.table(columns=columns_name, rows=rows,
                     row_key='id').classes('w-260').bind_filter_from(f, 'value')

    def add_row() -> None:

        if not select1.value or not select2.value:
            ui.notify(f'Faltan datos!!!')
            return False

        if not rows:
            new_id = 1
        else:
            new_id = max(dx['id'] for dx in rows) + 1
        autor = (con.mostrar_datos_by_id('autores', select1.value, 'nombre'))
        libro = (con.mostrar_datos_by_id('libros', select2.value, 'titulo'))

        rows.append({'id': new_id, 'autor_id': autor, 'libro_id': libro})
        ui.notify(f'Added in table {table_name} new row with ID {
                  new_id} autor {autor}, libro {libro}')
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
                       
                <q-td key="autor_id" :props="props">
                    {{ props.row.autor_id }}
                </q-td>
                <q-td key="libro_id" :props="props">
                    {{ props.row.libro_id }}
            </q-tr>
        ''')
    table.on('delete', delete)

    selec_value_libros, columns = con.mostrar_datos('libros', 'id, titulo')
    selector2_data = {}
    for x in selec_value_libros:
        selector2_data[x.get('id')] = x.get('titulo')

    selec_value_autor, columns = con.mostrar_datos('autores', 'id, nombre')
    selector1_data = {}
    for x in selec_value_autor:
        selector1_data[x.get('id')] = x.get('nombre')
    with ui.grid(columns=2):
        ui.label('Autor:')
        select1 = ui.select(selector1_data).classes('w-full')
        ui.label('Libro:')
        select2 = ui.select(selector2_data).classes('w-full')
        ui.button('Add row', icon='add', color='accent',
                  on_click=add_row).classes('w-full')

@ui.refreshable
def table_ejemplares(ui):
    table_name = 'ejemplares'
    con = Coneccion()
    rows, columns = con.mostrar_datos(table_name)
    columns_name = []
    for x in columns:
        columns_name.append(
            {'name': x, 'label': x, 'field': x, 'required': True})

    for x in rows:
        libro = (con.mostrar_datos_by_id(
            'libros', x.get('libro_id'), 'titulo'))
        x['libro_id'] = libro
    f = ui.input('Filter')
    table = ui.table(columns=columns_name, rows=rows,
                     row_key='id').classes('w-260').bind_filter_from(f, 'value')

    def add_row() -> None:

        if not select1.value or not select2.value:
            ui.notify(f'Faltan datos!!!')
            return False

        if not rows:
            new_id = 1
        else:
            new_id = max(dx['id'] for dx in rows) + 1

        libro = (con.mostrar_datos_by_id('libros', select2.value, 'titulo'))

        rows.append(
            {'id': new_id, 'localizacion': select1.value, 'libro_id': libro})
        ui.notify(f'Added in table {table_name} new row with ID {
                  new_id} localizacion {select1.value}, libro {select2.value}')
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
                <q-td key="localizacion" :props="props">
                    {{ props.row.localizacion }}
                </q-td>
                <q-td key="libro_id" :props="props">
                    {{ props.row.libro_id }}
            </q-tr>
        ''')
    table.on('delete', delete)

    selec_value_libros, columns = con.mostrar_datos('libros', 'id, titulo')
    selector2_data = {}
    for x in selec_value_libros:
        selector2_data[x.get('id')] = x.get('titulo')

    with ui.grid(columns=2):
        select1 = ui.input(label='localizacion',
                           placeholder='start typing', value='')
        ui.label('Libro:')
        select2 = ui.select(selector2_data).classes('w-full')
        ui.button('Add row', icon='add', color='accent',
                  on_click=add_row).classes('w-full')
    # with ui.card().tight():
    #     table_buscar_escribe(ui)

@ui.refreshable
def table_saca(ui):
    table_name = 'saca'
    con = Coneccion()
    rows, columns = con.mostrar_datos(table_name)
    columns_name = []
    for x in columns:
        if x == 'id':
            continue
        columns_name.append(
            {'name': x, 'label': x, 'field': x, 'required': True})

    for x in rows:
        alumno = (con.mostrar_datos_by_id(
            'alumnos', x.get('alumno_id'), 'nombre'))
        x['alumno_id'] = alumno
        
        # ejemplar_localizacion = (con.mostrar_datos_by_id('ejemplares', x.get('ejemplar_id'), 'localizacion'))
        # ejemplar_id = (con.mostrar_datos_by_id('ejemplares', x.get('ejemplar_id'), 'libro_id'))
        
        # nombre_libro = (con.mostrar_datos_by_id('libros', ejemplar_id, 'titulo'))
        # x['ejemplar_id'] = f"{ejemplar_localizacion} {nombre_libro}"
    
    f = ui.input('Filter')
    table = ui.table(columns=columns_name, rows=rows,
                     row_key='id').classes('w-260').bind_filter_from(f, 'value')

    def add_row() -> None:
        if not select1.value or not select2.value or not date1.value or not date2.value:
            ui.notify(f'Faltan datos!!!')
            return False

        if not rows:
            new_id = 1
        else:
            new_id = max(dx['id'] for dx in rows) + 1

        alumno_nombre = (con.mostrar_datos_by_id('alumnos', select1.value, 'nombre'))
        ejemplar_nombre = (con.mostrar_datos_by_id('ejemplares', select2.value))
        ejemplar_id = f"{ejemplar_nombre['localizacion']}"
        
        
        
        rows.append({'id': new_id, 'fecha_prestamo': date1.value, 'fecha_devolucion': date2.value,
                    'alumno_id': alumno_nombre, 'ejemplar_id': select2.value})
        


        ui.notify(f'Added in table {table_name} new row with ID {
                  new_id} localizacion {select1.value}, libro {select2.value}')
        con.inserta_datos_saca(table_name, date1.value,
                               date2.value, select1.value, select2.value)
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
                       
                <q-td key="fecha_prestamo" :props="props">
                    {{ props.row.fecha_prestamo }}
                </q-td>
                <q-td key="fecha_devolucion" :props="props">
                    {{ props.row.fecha_devolucion }}
                </q-td>
                <q-td key="alumno_id" :props="props">
                    {{ props.row.alumno_id }}
                </q-td>
                <q-td key="ejemplar_id" :props="props">
                    {{ props.row.ejemplar_id }}
                </q-td>
            </q-tr>
        ''')
    table.on('delete', delete)

    ejemplares, columns = con.mostrar_datos(
        'ejemplares', 'id, localizacion, libro_id')
    selector_ejemplares = {}
    for x in ejemplares:
        nombre_libro = con.mostrar_datos_by_id('libros', x.get('libro_id'))
        selector_ejemplares[x.get('id')] = f"{x.get('localizacion')}"

    alumnos, columns = con.mostrar_datos('alumnos', 'id, nombre')
    selector_alumnos = {}
    for x in alumnos:
        selector_alumnos[x.get('id')] = x.get('nombre')

    with ui.grid(columns=2):
        with ui.input('Fecha Prestamo') as date1:
            with date1.add_slot('append'):
                ui.icon('edit_calendar').on(
                    'click', lambda: menu.open()).classes('cursor-pointer')
            with ui.menu() as menu:
                ui.date().bind_value(date1)
        with ui.input('Fecha Devolucion') as date2:
            with date2.add_slot('append'):
                ui.icon('edit_calendar').on(
                    'click', lambda: menu.open()).classes('cursor-pointer')
            with ui.menu() as menu:
                ui.date().bind_value(date2)
        ui.label('Ejemplar ID:')
        select2 = ui.select(selector_ejemplares).classes('w-full')
        ui.label('Alumno ID:')
        select1 = ui.select(selector_alumnos).classes('w-full')
        ui.button('Add row', icon='add', color='accent',
                  on_click=add_row).classes('w-full')


# NICEGUI ZONE
# Creamos la cabecera.
with ui.header().classes(replace='row items-center') as header:
    # Formato de tabla
    ui.button(on_click=lambda: left_drawer.toggle(),
              icon='menu').props('flat color=white')
    # Creamos los tabs superiores
    with ui.tabs() as tabs:
        ui.tab('Alumnos')
        ui.tab('Libros')
        ui.tab('Escritores')
        ui.tab('Escribe')
        ui.tab('Ejemplares')
        ui.tab('Saca')

# Creamos el footer
with ui.footer(value=False) as footer:
    ui.label('Este es el footer y puede incluir info de contacto')

# creamos el panel izquierdo
with ui.left_drawer().classes('bg-green-50') as left_drawer:
    ui.label('Menu')
    with ui.tab_panels(tabs, value='Alumnos').classes('w-full'):
        with ui.tab_panel('Alumnos'):
            ui.label('En este menu puede agregar, borrar o buscar alumnos')
            ui.label('Si te quieres conectar ve a esta direccion.')
            link = f'http://{get_ip()}:8888'
            ui.link(link, link)
        with ui.tab_panel('Libros'):
            ui.label('En este menu puede agregar, borrar o buscar libros')
            ui.label('Si te quieres conectar ve a esta direccion.')
            link = f'http://{get_ip()}:8888'
            ui.link(link, link)
        with ui.tab_panel('Escritores'):
            ui.label('En este menu puede agregar, borrar o buscar escritores')
            ui.label('Si te quieres conectar ve a esta direccion.')
            link = f'http://{get_ip()}:8888'
            ui.link(link, link)
        with ui.tab_panel('Escribe'):
            ui.label('En este menu puede agregar, borrar o buscar escribe')
            ui.button('Refresh', on_click=table_escribe.refresh)
            ui.label('Si te quieres conectar ve a esta direccion.')
            link = f'http://{get_ip()}:8888'
            ui.link(link, link)
        with ui.tab_panel('Ejemplares'):
            ui.label('En este menu puede agregar, borrar o buscar ejemplares')
            ui.button('Refresh', on_click=table_ejemplares.refresh)
            ui.label('Si te quieres conectar ve a esta direccion.')
            link = f'http://{get_ip()}:8888'
            ui.link(link, link)
        with ui.tab_panel('Saca'):
            ui.label('En este menu puede agregar, borrar o buscar saca')
            ui.button('Refresh', on_click=table_saca.refresh)
            ui.label('Si te quieres conectar ve a esta direccion.')
            link = f'http://{get_ip()}:8888'
            ui.link(link, link)
# El footer lo pegamos al fondo
with ui.page_sticky(position='bottom-right', x_offset=10, y_offset=20):
    ui.button(on_click=footer.toggle, icon='contact_support').props('fab')

# Estos son los paneles principales y el value es cual es el default
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

    with ui.tab_panel('Saca'):
        # Con la UI creamos una tabla
        table_saca(ui)


# Ejecutamos la UI en el puerto 8888
ui.run(port=8888)

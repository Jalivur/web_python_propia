import reflex as rx
import psycopg2
from rxconfig import config
db_url=config.db_url


class contrasenas(rx.Model, table=True):
    sitio: str
    url_sitio: str
    usuario: str
    contraseña: str

class TableState(rx.State):

    contrasenas: list[dict] = []

    def load_data(self):
        conn = psycopg2.connect(db_url)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contrasenas")
        rows = cursor.fetchall()
        contrasenas={}
        for index, row in enumerate(rows):
            contrasenas[index] = {
            "id": row[0],
            "Sitio": row[1],
            "Url_sitio": row[2],
            "Usuario": row[3],
            "Contraseña": row[4]
            }
        cursor.close()
        return contrasenas
def tabla():
    state = TableState()
    state.load_data()
    print(state.load_data())
    dict_values= state.load_data.values()
    print(dict_values)
    columns = [

        {"title": "id", "type":"int"},
        {"title": "Sitio", "type":"str"},
        {"title": "Url_Sitio", "type":"str"},
        {"title": "Usuario", "type":"str"},
        {"title": "Contraseña", "type":"str"},
    ]
    return rx.data_table(
        data=dict_values.values(),
        columns=columns,
        pagination=True,
        search=True,
        sort=True,
    )
"""state= TableState()
state.load_data()
dict=vars(state)
import csv

# Supongamos que tienes el siguiente diccionario
diccionario = state.load_data

# Nombre del archivo CSV al que quieres exportar el diccionario
nombre_archivo = "mi_archivo.csv"

# Usamos el módulo csv para escribir en el archivo
with open(nombre_archivo, 'w') as f:
    writer = csv.DictWriter(f, fieldnames=diccionario.keys())
    writer.writeheader()
    writer.writerows(zip(*diccionario.values()))
"""
"""# Definición de las columnas para el DataEditor
columns: list[dict] = [
    {
        "title": "Columna 1",
        "type": "str",
    },
    {
        "title": "Columna 2",
        "type": "int",
    },
    # Agregar más columnas según sea necesario
]

# Datos que se quieren mostrar en la tabla
data: list[list[str]] = [
    ["dato1", 1],
    ["dato2", 2],
    # Agregar más filas de datos según sea necesario
]

# Componente DataEditor para mostrar los datos en formato de tabla
def your_data_table():
    return rx.data_editor(columns=columns, data=data)"""

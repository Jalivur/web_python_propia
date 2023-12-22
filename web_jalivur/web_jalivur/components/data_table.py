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
    columns: list[dict] = [
        "Id",
        "Sitio",
        "Url Sitio",
        "Usuario",
        "Contraseña",
        ]
    contrasenas: dict = []

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
    load_data=state.load_data()

    list_values=[list(dict_int.values()) for dict_int in load_data.values()]

    return rx.data_table(
        columns=TableState.columns,
        data=list_values,
        pagination=True,
        search=True,
        sort=False,
        resizable=True,
    )


import reflex as rx
import typing as tp
import psycopg2
from rxconfig import config
db_url=config.db_url
class editorstate():
    columns: list[dict[str, str]] = [
        {
            "title": "Id",
            "type": "int",
            "width":50,


        },
        {
            "title": "Sitio",
            "type": "str",
            "width":100,

        },
        {
            "title": "Url Sitio",
            "type": "str",
            "width":150,

        },
        {
            "title": "Usuario",
            "type": "str",
            "width":200,

        },
        {
            "title": "Contraseña",
            "type": "str",
            "width":800,

        },
    ]
    data: list[list] = [

    ]

    def load_data(self):
            conn = psycopg2.connect(db_url)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM contrasenas")
            rows = cursor.fetchall()
            print(rows)
            print(type(rows))
            for row in rows:
                rowl=list (row)
                self.data.append(rowl)
            cursor.close()
            conn.close()




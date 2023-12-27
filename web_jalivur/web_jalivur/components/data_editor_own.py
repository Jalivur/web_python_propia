import reflex as rx
import typing as tp
import psycopg2
import asyncio
from rxconfig import config
import time
db_url=config.db_url
class editorstate(rx.State):
    running: bool = False
    rate: int = 0.4
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
        },
        {
            "title": "Usuario",
            "type": "str",
            "width":180,
        },
        {
            "title": "Contraseña",
            "type": "str",
            "width":400,
        },
        {
            "title": "Fecha",
            "type": "str",
            "width":150,
        },
    ]
    data: list[list] = [

    ]




    @rx.background
    async def live_stream(self):
        conn = psycopg2.connect(db_url)
        cursor= conn.cursor()
        while self.running:
            await asyncio.sleep(1 / self.rate)  # Define la tasa de refresco
            if not self.running:
                break
            async with self:
                if len(self.data)>3000:  # Límite de filas en la tabla
                    self.data.pop(0)
                # Aquí realizarías la consulta a PostgreSQL para obtener los datos
                # Establece una conexión con la base de datos

                cursor.execute("SELECT * FROM contrasenas")  # Customize your query as needed
                records = cursor.fetchall()
                recordsl=[]
                for row in records:
                    rowl=list (row)
                    recordsl.append(rowl)
                if records:
                    self.data = recordsl


        cursor.close()
                # Cierra la conexión 
        conn.close()
        
    def toggle_pause(self):
        self.running = not self.running
        if self.running:
            return editorstate.live_stream
"""
    def load_data(self):
        conn = psycopg2.connect(db_url)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contrasenas")
        rows = cursor.fetchall()
        print(rows)
        for row in rows:
            rowl=list (row)
            self.data.append(rowl)
        cursor.close()
        conn.close()
"""





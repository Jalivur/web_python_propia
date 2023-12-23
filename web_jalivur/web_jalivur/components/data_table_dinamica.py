import reflex as rx
import asyncio
import psycopg2 # o la librería que prefieras para interactuar con PostgreSQL
from typing import Any, Dict, List
from rxconfig import config
db_url=config.db_url


class DataTableLiveState(rx.State):
    "The app state."

    running: bool = False
    table_data = []
    rate: int = 0.4
    columns: list[dict] = [
        "Id",
        "Sitio",
        "Url Sitio",
        "Usuario",
        "Contraseña",
        ]        

    @rx.background
    async def live_stream(self):
        conn = psycopg2.connect(db_url)
        cursor= conn.cursor()
        while True:
            await asyncio.sleep(1 / self.rate)  # Define la tasa de refresco
            if not self.running:
                break
            async with self:
                if len(self.table_data):  # Límite de filas en la tabla
                    self.table_data.pop(0)
                # Aquí realizarías la consulta a PostgreSQL para obtener los datos
                # Establece una conexión con la base de datos
   
                cursor.execute("SELECT * FROM contrasenas")  # Customize your query as needed
                records = cursor.fetchall()
                print(type(records))

                if records:
                    self.table_data = records
        cursor.close()
                # Cierra la conexión 
        conn.close()
    def toggle_pause(self):
        self.running = not self.running
        if self.running:
            return DataTableLiveState.live_stream





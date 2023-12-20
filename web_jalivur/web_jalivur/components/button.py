import reflex as rx
from rxconfig import config
import psycopg2

db_url=config.db_url
class State(rx.State):
    
    # Define any necessary state variables and methods here

    def on_submit(self):
        conn = psycopg2.connect(db_url)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contrasenas")
        rows = cursor.fetchall()
        data_dict={}
        for index, row in enumerate(rows):
            data_dict[index] = {
            "id": row[0],
            "Sitio": row[1],
            "Url_sitio": row[2],
            "Usuario": row[3],
            "Contraseña": row[4]
            }
        cursor.close()
        print(data_dict)
        return data_dict



    
rx.button(
        "Submit",
        on_click=print(State.on_submit), # Assign the event handler
        # Add any additional styling or properties here
    )
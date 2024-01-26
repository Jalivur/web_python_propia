import reflex as rx
import psycopg2
import datetime
from rxconfig import config
from web_jalivur.styles.styles import Size, Color
from web_jalivur.styles.colors import Color, TextColor
from web_jalivur.styles.fonts import Font

db_url=config.db_url

class FormState(rx.State):
    form_data: dict = {}
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        conn = psycopg2.connect(db_url)

        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS contrasenas (id SERIAL PRIMARY KEY, Sitio TEXT, Url_sitio TEXT, Usuario TEXT, Contraseña TEXT, Lugar_Has TEXT, Fecha TEXT)")
        conn.commit()
        cursor.close()

        cursor = conn.cursor()
        Sitio= form_data.get("Sitio")
        Url_sitio = form_data.get("Url")
        Usuario = form_data.get("Usuario")
        Contraseña = form_data.get("Contraseña")
        lugar_has = form_data.get("lugar")
        date= datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        sql= (f"INSERT INTO contrasenas (Sitio, Url_sitio, Usuario, Contraseña, Lugar_Has, Fecha) VALUES ('{Sitio}', '{Url_sitio}', '{Usuario}', '{Contraseña}','{lugar_has}','{date}')")
        cursor.execute(sql)
        conn.commit()
        cursor.close()

def form(title:str):
    return rx.vstack(
        rx.box(rx.text(title, as_="strong", font_size=Size.MEDIUM.value, text_color=TextColor.ACCENT.value), class_name="nes-balloon from-right is-dark"),
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Sitio",
                    name="Sitio",
                    is_required = True,
                ),
                rx.input(
                    placeholder="Url Sitio",
                    name="Url",
                    is_required = True,
                ),
                rx.input(
                    placeholder="Usuario",
                    name="Usuario",
                    is_required = True,
                ),
                rx.input(
                    placeholder="Contraseña",
                    name="Contraseña",
                    is_required = True,
                ),
                rx.input(
                    placeholder="Lugar Has",
                    name="lugar",
                    is_required = True,
                ),
                rx.button("Submit", type_="submit", class_name="nes-btn is-success"),
                height="100%",
                width="90%",
                class_name="nes-table is-bordered is-dark"
            ),
            on_submit=FormState.handle_submit,
            reset_on_submit=True,
        ),
        )

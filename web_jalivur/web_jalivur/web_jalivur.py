"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
from web_jalivur.components.nav_bar import navbar
#from web_jalivur.views.header.header import header
#from web_jalivur.views.links.links import links
from web_jalivur.components.footer import footer
import web_jalivur.styles.styles as styles
from web_jalivur.components.forms import form
import psycopg2

db_url=config.db_url
docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass
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


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.card(
            rx.box(
                rx.center(rx.text("Tarjeta formulario")),
                form("Generador de Contraseña"),
            ),
            align="center",
        ),
        rx.button("busqueda",on_click=State.on_submit()),
        footer()
    )

# Add state and page to the app.
app = rx.App(
    style= styles.BASE_STYLE
) 
app.add_page(index)
app.compile()

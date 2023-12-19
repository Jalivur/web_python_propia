import reflex as rx
import psycopg2
class FormState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        conn = psycopg2.connect( 
        host="mydatabase-esteya92-1cl.a.aivencloud.com",
        database="defaultdb",
        user="avnadmin",
        password="AVNS_xOf_0MRXzrrUYS8IaDf",
        port="15904"
        )
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS contrasenas (id SERIAL PRIMARY KEY, Sitio TEXT, Url_sitio TEXT, Usuario TEXT, Contraseña TEXT)")
        conn.commit()
        cursor.close()

        cursor = conn.cursor()
        Sitio= form_data.get("Sitio")
        Url_sitio = form_data.get("Url")
        Usuario = form_data.get("Usuario")
        Contraseña = form_data.get("Contraseña")
        sql= (f"INSERT INTO contrasenas (Sitio, Url_sitio, Usuario, Contraseña) VALUES ('{Sitio}', '{Url_sitio}', '{Usuario}', '{Contraseña}')")
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contrasenas")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        cursor.close()


def form(title:str):
    return rx.vstack(
        rx.text(title, as_="strong", font_size="2em"),
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
                rx.button("Submit", type_="submit"),

            ),

            on_submit=FormState.handle_submit,
            reset_on_submit=True,
        ),
            rx.divider(),
            rx.heading("Results"),
            rx.text(FormState.form_data.to_string()),
        )

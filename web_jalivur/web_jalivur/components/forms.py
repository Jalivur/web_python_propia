import reflex as rx
import psycopg2



class DynamicFormState(rx.State):
    form_data: dict = {}
    form_fields: list[str] = [
        "Sitio",
        "Url_sitio",
        "Usuario",
        "Contraseña"
    ]

    @rx.cached_var
    def form_field_placeholders(self) -> list[str]:
        return [
            " ".join(
                w.capitalize() for w in field.split("_")
            )
            for field in self.form_fields
        ]

    def add_field(self, form_data: dict):
        new_field = form_data.get("new_field")
        if not new_field:
            return
        field_name = (
            new_field.strip().lower().replace(" ", "_")
        )
        self.form_fields.append(field_name)

    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        

def dynamic_form(title: str):
    return rx.vstack(
        rx.text(title, as_="strong", font_size="4em"),
        rx.form(
            rx.vstack(
                rx.foreach(
                    DynamicFormState.form_fields,
                    lambda field, idx: rx.input(
                        placeholder=DynamicFormState.form_field_placeholders[
                            idx
                        ],
                        name=field,
                        is_required=True
                    ),
                ),
                rx.button("Submit", type_="submit"),
            ),
            on_submit=DynamicFormState.handle_submit,
            reset_on_submit=True,
        ),
        rx.form(
            rx.hstack(
                rx.input(
                    placeholder="New Field",
                    name="new_field",
                ),
                rx.button("+", type_="submit"),
            ),
            on_submit=DynamicFormState.add_field,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.heading("Resultados"),
        rx.text(DynamicFormState.form_data.to_string()),
    )

class FormState_entry(rx.State):
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
        Url_sitio = form_data.get("Url_sitio")
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


def form_entry(title:str):
    return rx.vstack(
        rx.text(title, as_="strong", font_size="2em"),
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Sitio",
                    name="Sitio",
                ),
                rx.input(
                    placeholder="Url Sitio",
                    url="Url_Sitio",
                ),
                rx.input(
                    placeholder="Usuario",
                    usuario="Usuario",
                ),
                rx.input(
                    placeholder="Contraseña",
                    contrasena="Contraseña",
                ),
                """rx.hstack(
                    rx.checkbox("Checked", name="check"),
                    rx.switch("Switched", name="switch"),"""
                ),
                rx.button("Submit", type_="submit"),
            ),
            on_submit=FormState_entry.handle_submit,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(FormState_entry.form_data.to_string()),
    )

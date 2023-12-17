import reflex as rx


class DynamicFormState(rx.State):
    form_data: dict = {}
    form_fields: list[str] = [
        "Sitio",
        "URL Sitio",
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
        #rx.heading("Resultados"),
        #rx.text(DynamicFormState.form_data.to_string()),
    )
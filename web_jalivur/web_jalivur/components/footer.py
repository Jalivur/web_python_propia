import reflex as rx
import datetime
def footer() -> rx.Component:
    return  rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            f"© 2023-{datetime.date.today().year} Jalivur by Alberto Estella V1.",
            href="https://github.com/Jalivur",
            is_external=True
            ),
        rx.text("studying development with 🎊"),
        rx.link("mouredev",
                href="https://moure.dev",
                is_external= True,
                )
    )
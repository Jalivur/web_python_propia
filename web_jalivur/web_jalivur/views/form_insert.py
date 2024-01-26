import reflex as rx
import web_jalivur.styles.colors as colors
from web_jalivur.components.forms import form

def form_page():
    return rx.vstack(
                    rx.vstack(
                        rx.vstack(
                            rx.card(
                                rx.vstack(
                                    form("Insercion de Contraseña"),
                                class_name="nes-container is-dark with-title",
                                ),
                            background_color=colors.Color.ACCENT.value,
                            ),
                        ),
                    ),

            )
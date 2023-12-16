"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Jalivur",
            height = "50px",
            color = "white"

        
        ),
        position = "sticky",
        bg="red",
        padding_x = "10px",
        padding_y = "10px",
        z_index ="999"
    )

# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()

"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
from web_jalivur.components.nav_bar import navbar
from web_jalivur.views.header.header import header
from web_jalivur.views.links.links import links
from web_jalivur.components.footer import footer
import web_jalivur.styles.styles as styles
docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
            header(),
            links(),
            max_width=styles.MAX_WIDTH,
            width="100%",
            margin_y=styles.Spacer.BIG.value
            )
        ),
        footer()
    )

# Add state and page to the app.
app = rx.App(
    style= styles.BASE_STYLE
) 
app.add_page(index)
app.compile()

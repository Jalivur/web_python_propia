"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
import functools
import json
import os
import time
from web_jalivur.components.react_oauth_google import GoogleOAuthProvider, GoogleLogin
from google.auth.transport import requests
from google.oauth2.id_token import verify_oauth2_token

import reflex as rx
from web_jalivur.components.nav_bar import navbar
#from web_jalivur.views.header.header import header
#from web_jalivur.views.links.links import links
from web_jalivur.components.footer import footer
import web_jalivur.styles.styles as styles
import web_jalivur.styles.colors as colors
from web_jalivur.components.forms import form
from web_jalivur.components.data_table import tabla


CLIENT_ID="926775887168-m5l5sk0umb5n2ft4991qle6q92mdvdu9.apps.googleusercontent.com"
db_url=config.db_url
docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    id_token_json: str = rx.LocalStorage()

    def on_success(self, id_token: dict):
        self.id_token_json = json.dumps(id_token)

    @rx.cached_var
    def tokeninfo(self) -> dict[str, str]:
        try:
            return verify_oauth2_token(
                json.loads(self.id_token_json)["credential"],
                requests.Request(),
                CLIENT_ID,
            )
        except Exception as exc:
            if self.id_token_json:
                print(f"Error verifying token: {exc}")
        return {}

    def logout(self):
        self.id_token_json = ""

    @rx.var
    def token_is_valid(self) -> bool:
        try:
            return bool(
                self.tokeninfo
                and int(self.tokeninfo.get("exp", 0)) > time.time()
            )
        except Exception:
            return False

    @rx.cached_var
    def Welcome_content(self) -> str:
        if self.token_is_valid:
            return f"Biembenido, Me alegro de Verte {self.tokeninfo['name']}"
        return "NO ESTAS AUTORIZADO!!!!! LARGO DE AQUI!!!!"


def user_info(tokeninfo: dict) -> rx.Component:
    return rx.hstack(
        rx.avatar(
            name=tokeninfo["name"],
            src=tokeninfo["picture"],
            size="md",
        ),
        rx.vstack(
            rx.heading(tokeninfo["name"], size="sm", text_align="justified"),
            rx.text(tokeninfo["email"], font_size="1em"),
            align_items="justified",
            width="100%"
        ),
        rx.button("Logout", on_click=State.logout, text_color= colors.TextColor.SECONDARY.value, bg=colors.Color.ACCENT.value),
        padding="10px",
    )


def login() -> rx.Component:
    return rx.vstack(
        GoogleLogin.create(on_success=State.on_success),
    )


def require_google_login(page) -> rx.Component:
    @functools.wraps(page)
    def _auth_wrapper() -> rx.Component:
        return GoogleOAuthProvider.create(
            rx.cond(
                State.is_hydrated,
                rx.cond(State.token_is_valid, page(), login()),
                rx.spinner(),
            ),
            client_id=CLIENT_ID,
        )
    return _auth_wrapper


def index() -> rx.Component:
    return rx.vstack(
        rx.heading("Bienvenido la Web de Jalivur", size="lg"),
        rx.link("Welcome Page", href="/Welcome_page"),
    )
@rx.page(route="/Welcome_page")
@require_google_login
def Welcome() -> rx.Component:
    return rx.vstack(
        user_info(State.tokeninfo),
        rx.text(State.Welcome_content, font_size="3em", font_tipe="strong"),
        rx.link("Formulario Inserción", href="/Formulario"),
        rx.link("Tabla", href="/Tabla", font_size=styles.Size.BIG.value),
        rx.link("Volver", href="/")
    )
@rx.page(route="/Formulario")
@require_google_login
def form_insert() -> rx.Component:
    return rx.box(
                navbar(),
                rx.vstack(
                rx.link("Volver", href="/Welcome_page"),
                rx.box(
                rx.card(
                    rx.box(
                        form("Insercion de Contraseña"),
                    ),
                    align="center",
                    background= styles.Color.SECONDARY.value
                ),
                footer()
                ),
            ),
            width="100%",
        )
@rx.page(route="/Tabla")
@require_google_login
def data_table() -> rx.Component:
    return rx.vstack(
        rx.link("Volver", href="/Welcome_page"),
        rx.box(
            tabla(),
            width="95%",
        )
    )

# Add state and page to the app.
app = rx.App(

    stylesheets= styles.STILESHEETS,
    style= styles.BASE_STYLE    
) 
app.add_page(index)
app.add_page(data_table)
app.add_page(Welcome)
app.compile()

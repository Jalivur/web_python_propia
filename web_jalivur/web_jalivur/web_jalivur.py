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
#from web_jalivur.components.data_table_dinamica import DataTableLiveState
import web_jalivur.styles.fonts as Fonts
from web_jalivur.components.data_editor_own import editorstate
dark_theme = {
    "accent_color": "#8c96ff",
    "accent_light": "rgba(202, 206, 255, 0.253)",
    "text_dark": "#ffffff",
    "text_medium": "#b8b8b8",
    "text_light": "#a0a0a0",
    "text_bubble": "#ffffff",
    "bg_icon_header": "#b8b8b8",
    "fg_icon_header": "#000000",
    "text_header": "#a1a1a1",
    "text_header_selected": "#000000",
    "bg_cell": "#16161b",
    "bg_cell_medium": "#202027",
    "bg_header": "#212121",
    "bg_header_has_focus": "#474747",
    "bg_header_hovered": "#404040",
    "bg_bubble": "#212121",
    "bg_bubble_selected": "#000000",
    "bg_search_result": "#423c24",
    "border_color": "rgba(225,225,225,0.2)",
    "drilldown_border": "rgba(225,225,225,0.4)",
    "link_color": "#4F5DFF",
    "header_font_style": "bold 18px",
    "base_font_style": "16px",
    "font_family": "Inter, Roboto, -apple-system, BlinkMacSystemFont, avenir next, avenir, segoe ui, helvetica neue, helvetica, Ubuntu, noto, arial, sans-serif",
}








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
            show_border= True,
            border_color= colors.Color.SECONDARY.value
        ),
        rx.vstack(
            rx.heading(tokeninfo["name"],class_name="nes-text is-primary", size="xs", text_align="justified", font_family= Fonts.Fonts.DEFAULT.value),
            rx.text(tokeninfo["email"], font_size="0.7em",class_name="nes-text is-disabled"),
            align_items="justified",
            width="60%"
        ),
        rx.button("Logout", size="sm",class_name="nes-btn is-warning", on_click=State.logout, text_color= colors.TextColor.SECONDARY.value, bg=colors.Color.ACCENT.value),
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
        rx.heading("Bienvenido a la Web de Jalivur", class_name="nes-text is-success", font_family= Fonts.Fonts.DEFAULT.value, size="lg"),
        rx.link("Welcome Page", href="/Welcome_page"),
        class_name="nes-container is-rounded is-dark",
        align_items="center",
        width="100%",
        margin="20%"
    )

@rx.page(route="/Welcome_page")
@require_google_login
def Welcome() -> rx.Component:
    return rx.vstack(
        user_info(State.tokeninfo),
        rx.text(State.Welcome_content, class_name="nes-text is-success", font_size=styles.Size.INTERMEDIATE.value, font_tipe="strong"),
        rx.link("Formulario Inserción", class_name="nes-text is-primary", href="/Formulario", font_size=styles.Size.INTERMEDIATE.value),
        #rx.link("Tabla", href="/Tabla", class_name="nes-text is-primary", font_size=styles.Size.INTERMEDIATE.value),
        rx.link("Tabla Editable", href="/tabla_nueva"),
        rx.link("Volver", href="/", class_name="nes-text is-disabled"),
        )

@rx.page(route="/Formulario")
@require_google_login
def form_insert() -> rx.Component:
    return rx.box(
                navbar(),
                rx.link("Volver", href="/Welcome_page", color=styles.TextColor.TERTIARY.value),
                rx.vstack(
                rx.box(
                rx.card(
                    rx.box(
                        form("Insercion de Contraseña"),
                        class_name="nes-table is-bordered is-darck",
                    ),
                    align="center",
                    backgroud_color=styles.Color.SECONDARY.value
                ),
                footer()
                ),
            ),
            width="100%",
        )


@rx.page(route="/tabla_nueva")
@require_google_login
def tabla_editable() -> rx.Component:
    return rx.vstack(
            rx.stack(
        rx.cond(
            ~editorstate.running,
            rx.button("Start", on_click=editorstate.toggle_pause, class_name="nes-btn is-success"),
            rx.button("Pause", on_click=editorstate.toggle_pause, class_name="nes-btn is-error"),
        ),
    ),
        rx.center(
        rx.data_editor(
            columns=editorstate.columns,
            data=editorstate.data,
            theme=dark_theme,

        ),
    ),
        rx.link("Volver", href="/Welcome_page", color=styles.TextColor.TERTIARY.value),
        width="100%",
        class_name="nes-table-responsive"

    )
# Add state and page to the app.
app = rx.App(

    stylesheets= styles.STILESHEETS,
    style= styles.BASE_STYLE    
) 
app.add_page(index)
app.add_page(Welcome)
app.compile()

"""
@rx.page(route="/Tabla")
@require_google_login
def data_table() -> rx.Component:
    return rx.vstack(
    rx.link("Volver", href="/Welcome_page", color=styles.TextColor.TERTIARY.value),
    rx.stack(
        rx.cond(
            ~DataTableLiveState.running,
            rx.button("Start", on_click=DataTableLiveState.toggle_pause, class_name="nes-btn is-success"),
            rx.button("Pause", on_click=DataTableLiveState.toggle_pause, class_name="nes-btn is-error"),
        ),
    ),
    rx.center(
     rx.data_table(
        columns=DataTableLiveState.columns,
        data=DataTableLiveState.table_data,

        ),
        widht="98%"
    )
)
"""
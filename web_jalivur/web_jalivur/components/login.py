#Importacion componentes necesarios para login google
import reflex as rx
from web_jalivur.components.react_oauth_google import GoogleOAuthProvider, GoogleLogin
from google.auth.transport import requests
from google.oauth2.id_token import verify_oauth2_token
import web_jalivur.styles.fonts as Fonts
import web_jalivur.styles.colors as colors
import functools
import json
import time
CLIENT_ID="926775887168-m5l5sk0umb5n2ft4991qle6q92mdvdu9.apps.googleusercontent.com"
#Clase definida, para login google
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
                    rx.heading(
                        tokeninfo["name"],
                        class_name="nes-text is-primary", 
                        size="xs", text_align="justified", 
                        font_family= Fonts.Font.DEFAULT.value,
                        ),
                    rx.text(
                        tokeninfo["email"], 
                        font_size="0.7em",
                        class_name="nes-text is-disabled",
                        ),
                    align_items="justified",
                    width="60%"
                ),
                rx.button(
                    "Logout", 
                    size="sm",
                    class_name="nes-btn is-warning",
                    on_click=State.logout, 
                    text_color= colors.TextColor.SECONDARY.value, 
                    bg=colors.Color.ACCENT.value,
                    ),
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
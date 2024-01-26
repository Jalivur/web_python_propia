"""Welcome to Reflex! This file outlines the steps to create a basic app."""
#Configuracion y modulo principal reflex
from rxconfig import config
import reflex as rx
import web_jalivur.styles.styles as styles

#importacion modulos propios
from web_jalivur.components.nav_bar import navbar
from web_jalivur.components import login
from web_jalivur.views.index import index_page
from web_jalivur.views.welcome import welcome_page
from web_jalivur.views.form_insert import form_page
from web_jalivur.views.gen_encript import gen_enc_page
from web_jalivur.views.tabla import tabla_page
from web_jalivur.components.footer import footer


#Configuracion Acceso a Db remoto
db_url=config.db_url
#Url a documentaicon reflex
docs_url = "https://reflex.dev/docs/getting-started/introduction"
#Variable nombre archivo
filename = f"{config.app_name}/{config.app_name}.py"



#Pagina de inicio, desde la que hacer login
@rx.page(route="/")
def index() -> rx.Component:
    return rx.vstack(
            index_page(),
            footer(),
    )
#Pagina de Bienvenida tras el login
@rx.page(route="/Welcome_page")
@login.require_google_login
def Welcome() -> rx.Component:
    return rx.vstack(
        welcome_page(),
        footer(),
            )
    
#Pagina Formulario de insercion de datos
@rx.page(route="/Formulario")
@login.require_google_login
def form_insert() -> rx.Component:
    return rx.vstack(
        navbar(),
        form_page(),
        footer(),
            )

@rx.page(route="/encrypt")
@login.require_google_login
def gen_encrypt() -> rx.Component:
    return rx.vstack(
                    navbar(),
                    gen_enc_page(),
                    footer(),
            )



@rx.page(route="/tabla")
@login.require_google_login
def tabla_editable() -> rx.Component:
    return rx.vstack(
                    navbar(),
                    tabla_page(),
                    footer(),
            )
# Add state and page to the app.
app = rx.App(
    stylesheets= styles.STILESHEETS,
    style= styles.BASE_STYLE,
) 
app.add_page(index)
app.add_page(Welcome)
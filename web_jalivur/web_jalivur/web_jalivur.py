"""Welcome to Reflex! This file outlines the steps to create a basic app."""
#Configuracion y modulo principal reflex
from rxconfig import config
import reflex as rx

#importacion modulos propios
from web_jalivur.components.nav_bar import navbar
from web_jalivur.components.footer import footer
import web_jalivur.styles.styles as styles
import web_jalivur.styles.colors as colors
from web_jalivur.components.forms import form
import web_jalivur.styles.fonts as Font
from web_jalivur.components.data_editor_own import editorstate
import web_jalivur.styles.themes as theme
from web_jalivur.components.passgen import NumberInputState
from web_jalivur.components.encrypt_pass import MsgInputState
from web_jalivur.components import login


#Configuracion Acceso a Db remoto
db_url=config.db_url
#Url a documentaicon reflex
docs_url = "https://reflex.dev/docs/getting-started/introduction"
#Variable nombre archivo
filename = f"{config.app_name}/{config.app_name}.py"



#Pagina de inicio, desde la que hacer login
def index() -> rx.Component:
    return rx.vstack(
                    rx.heading(
                        "Bienvenido a la Web de Jalivur", 
                        class_name="nes-text is-success", 
                        font_family= Font.Font.DEFAULT.value, 
                        size="lg",
                        ),
                        #Navegacion hasta pagina de Bienvenida
                    rx.link(
                            "Welcome Page", 
                            href="/Welcome_page",
                            ),
                class_name="nes-container is-rounded is-dark",
                align_items="center",
                width="100%",
                margin="20%"
            )
#Pagina de Bienvenida tras el login
@rx.page(route="/Welcome_page")
@login.require_google_login
def Welcome() -> rx.Component:
    return rx.vstack(
                    login.user_info(login.State.tokeninfo),
                    rx.text(
                            #Contenido bienvenida login
                            login.State.Welcome_content, 
                            class_name="nes-text is-success", 
                            font_size=styles.Size.MEDIUM.value, 
                            font_tipe="strong",
                            ),
                    rx.link(
                            #Enlace a pagina formulario insercion datos
                            "Formulario Inserción", 
                            class_name="nes-text is-primary", 
                            href="/Formulario", 
                            font_size=styles.Size.MEDIUM.value,
                            ),
                    rx.link(
                            #Enlace a pagina Tabla de datos de db remoto
                            "Tabla", 
                            href="/tabla", 
                            class_name="nes-text is-primary",
                            ),
                    rx.link(
                            #Enlace a pagina de generacion encriptado y desencriptado de contraseñas
                            "Generado y Encryptador", 
                            href="/encrypt", 
                            class_name="nes-text is-primary",
                            ),
                    rx.link(
                            #Volver a pagina de inicio
                            "Volver", 
                            href="/", 
                            class_name="nes-text is-disabled",
                            ),
                    #modulo propio pie de pagina
                    footer(),
            )
#Pagina Formulario de insercion de datos
@rx.page(route="/Formulario")
@login.require_google_login
def form_insert() -> rx.Component:
    return rx.vstack(
                    navbar(),
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

@rx.page(route="/encrypt")
@login.require_google_login
def gen_encrypt() -> rx.Component:
    return rx.vstack(
                    navbar(),
                    rx.vstack(
                        rx.text(
                                "Lonigtud contraseña a geneara",
                                ),
                        rx.number_input(
                                on_change=NumberInputState.set_number,
                                default_value=6,
                                min_=6,
                            ),
                        rx.button(
                                "Generar", 
                                on_click=NumberInputState.generar_contrasena, 
                                class_name="nes-btn is-success",
                                ),
                        rx.text("Contraseña generada"),
                        rx.text_area(
                                value=NumberInputState.contrasena, 
                                width="auto",
                                ),
                        class_name="nes-container is-rounded is-dark",
                    ),
                    rx.button(
                            "Limpiar", 
                            on_click=NumberInputState.clear(), 
                            class_name="nes-btn is-warning",
                            ),
                    rx.desktop_only(
                            rx.hstack(
                                    rx.vstack(
                                    rx.text("Mensage a encriptar"),
                                    rx.text_area(
                                            value=MsgInputState.msg_in,
                                            on_change=MsgInputState.set_msg_in,
                                            width="auto",
                                    ),
                                    rx.text("Clave salida"),
                                    rx.text_area(
                                            value=MsgInputState.clave_out, 
                                            width="auto",
                                            ),
                                    rx.text("Mensage encriptado"),
                                    rx.text_area(
                                            value=MsgInputState.msghas_out, 
                                            width="auto",
                                            ),
                                    rx.button(
                                            "Encriptar",
                                            on_click=MsgInputState.encriptar(),
                                            class_name="nes-btn is-success",
                                            ),
                                    class_name="nes-container is-rounded is-dark",
                                    ),
                                    rx.vstack(
                                    rx.text("Mensage a desencriptar"),
                                    rx.text_area(
                                            value=MsgInputState.msghas_in,
                                            on_change=MsgInputState.set_msghas_in,
                                            width="auto",
                                    ),
                                    rx.text("Clave entrada"),
                                    rx.text_area(
                                            value=MsgInputState.clave_in,
                                            on_change=MsgInputState.set_clave_in,
                                            width="auto"
                                    ),
                                    rx.text("Mensage desencriptado"),
                                    rx.text_area(
                                            value=MsgInputState.msg_out, 
                                            width="auto",
                                            ),
                                    rx.button(
                                            "Desencriptar",
                                            on_click=MsgInputState.desencriptar(),
                                            class_name="nes-btn is-error",
                                            ),
                                    class_name="nes-container is-rounded is-dark",
                                    ),
                                    max_width="100vw",
                            ),
                            ),
                    rx.mobile_and_tablet(
                        rx.vstack(
                                rx.vstack(
                                    rx.text("Mensage a encriptar"),
                                    rx.text_area(
                                            value=MsgInputState.msg_in,
                                            on_change=MsgInputState.set_msg_in,
                                            width="auto",
                                    ),
                                    rx.text("Clave salida"),
                                    rx.text_area(
                                            value=MsgInputState.clave_out, 
                                            width="auto",
                                            ),
                                    rx.text("Mensage encriptado"),
                                    rx.text_area(
                                            value=MsgInputState.msghas_out, 
                                            width="auto",
                                            ),
                                    rx.button(
                                            "Encriptar",
                                            on_click=MsgInputState.encriptar(),
                                            class_name="nes-btn is-success",
                                            ),
                                class_name="nes-container is-rounded is-dark",
                                ),
                                rx.vstack(
                                    rx.text("Mensage a desencriptar"),
                                    rx.text_area(
                                            value=MsgInputState.msghas_in,
                                            on_change=MsgInputState.set_msghas_in,
                                            width="auto",
                                    ),
                                    rx.text("Clave entrada"),
                                    rx.text_area(
                                            value=MsgInputState.clave_in,
                                            on_change=MsgInputState.set_clave_in,
                                            width="auto"
                                    ),
                                    rx.text("Mensage desencriptado"),
                                    rx.text_area(
                                            value=MsgInputState.msg_out, 
                                            width="auto",
                                            ),
                                    rx.button(
                                            "Desencriptar",
                                            on_click=MsgInputState.desencriptar(),
                                            class_name="nes-btn is-error",
                                            ),
                                class_name="nes-container is-rounded is-dark",
                                ),
                                max_width="100vw",
                            ),
                        
                        ),
                    rx.button(
                            "Limpiar", 
                            on_click=MsgInputState.limpiar(), 
                            class_name="nes-btn is-warning",
                            ),
                                    max_height="100vw", 
            )



@rx.page(route="/tabla")
@login.require_google_login
def tabla_editable() -> rx.Component:
    return rx.vstack(
                    navbar(),
                    rx.stack(
                            rx.cond(
                                    ~editorstate.running,
                                    rx.button(
                                            "Start", 
                                            on_click=editorstate.toggle_pause, 
                                            class_name="nes-btn is-success",
                                            ),
                                    rx.button(
                                            "Pause", 
                                            on_click=editorstate.toggle_pause, 
                                            class_name="nes-btn is-error",
                                            ),
                            ),
                    ),
                    rx.box(
                        rx.data_editor(
                            columns=editorstate.columns,
                            data=editorstate.data,
                            freeze_columns=2,
                            smooth_scroll_x=True,
                            #smooth_scroll_y=True,
                            #overflow="auto",
                            overscroll_x=50,
                            #row_markers='clickable-number',
                            row_height=50,
                            theme=theme.futuristic_dark_theme,
                            
                        ),
                        max_width="90%",
                        position="relative",
                        padding="2%",
                        #left="",
                    ),

            )
# Add state and page to the app.
app = rx.App(
    stylesheets= styles.STILESHEETS,
    style= styles.BASE_STYLE,
) 
app.add_page(index)
app.add_page(Welcome)
#app.compile()

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
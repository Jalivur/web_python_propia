import reflex as rx
import web_jalivur.styles.styles as styles
from web_jalivur.components import login

def welcome_page():
    return rx.vstack(
                    login.user_info(login.State.tokeninfo),
                    rx.text(
                            #Contenido bienvenida login
                            login.State.Welcome_content, 
                            class_name="nes-text is-success", 
                            font_size=styles.Size.LARGE.value, 
                            font_tipe="strong",
                            text_align="center"
                            ),
                    rx.vstack(
                    rx.link(
                            #Enlace a pagina formulario insercion datos
                            "---Formulario Inserción---", 
                            class_name="nes-text is-primary", 
                            href="/Formulario", 
                            font_size=styles.Size.DEFAULT.value,
                            padding="50px",
                            text_align="center",
                            width="90vw",
                            height="50px"
                            ),
                    rx.link(
                            #Enlace a pagina Tabla de datos de db remoto
                            "---Tabla---", 
                            href="/tabla", 
                            class_name="nes-text is-primary",
                            font_size=styles.Size.DEFAULT.value,
                            padding="50px",
                            text_align="center",
                            width="90vw",
                            height="50px"
                            ),
                    rx.link(
                            #Enlace a pagina de generacion encriptado y desencriptado de contraseñas
                            "---Generado y Encryptador---", 
                            href="/encrypt", 
                            class_name="nes-text is-primary",
                            font_size=styles.Size.DEFAULT.value,
                            padding="50px",
                            text_align="center",
                            width="90vw",
                            height="50px"
                            ),
                    rx.link(
                            #Volver a pagina de inicio
                            "---Volver---", 
                            href="/", 
                            class_name="nes-text is-primary",
                            font_size=styles.Size.DEFAULT.value,
                            padding="50px",
                            text_align="center",
                            width="90vw",
                            height="50px"
                            ),
                    ),
    )
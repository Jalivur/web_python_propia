import reflex as rx
import web_jalivur.styles.fonts as Font

def index_page():
    return rx.vstack(
                    rx.heading(
                        "Bienvenido a la Web de Jalivur", 
                        class_name="nes-text is-success", 
                        font_family= Font.Font.DEFAULT.value, 
                        size="lg",
                        text_align="center",
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
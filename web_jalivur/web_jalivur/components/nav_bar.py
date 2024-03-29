import reflex as rx
import web_jalivur.styles.styles as styles
import web_jalivur.styles.colors as color

def navbar() -> rx.Component:
    return rx.responsive_grid(
            rx.desktop_only(
                rx.hstack(
                    rx.divider(
                            orientation="horizontal", 
                            variant="dashed", 
                            border_color=color.Color.ACCENT.value, 
                            ),
                    rx.link(
                            #Enlace a pagina formulario insercion datos
                            "Formulario Inserción", 
                            class_name="nes-text is-error", 
                            href="/Formulario", 
                            font_size=styles.Size.DEFAULT.value,
                            ),
                    rx.divider(
                            orientation="horizontal", 
                            variant="dashed", 
                            border_color=color.Color.ACCENT.value, 
                            ),
                    rx.link(
                            #Enlace a pagina Tabla de datos de db remoto
                            "Tabla", 
                            href="/tabla", 
                            class_name="nes-text is-error",
                            font_size=styles.Size.DEFAULT.value,
                            ),
                    rx.divider(
                            orientation="horizontal", 
                            variant="dashed", 
                            border_color=color.Color.ACCENT.value, 
                            ),
                    rx.link(
                            #Enlace a pagina de generacion encriptado y desencriptado de contraseñas
                            "Generado y Encryptador", 
                            href="/encrypt", 
                            class_name="nes-text is-error",
                            font_size=styles.Size.DEFAULT.value,
                            ),
                    rx.divider(
                            orientation="horizontal", 
                            variant="dashed", 
                            border_color=color.Color.ACCENT.value, 
                            ),
                    rx.link(
                            "Volver", 
                            href="/Welcome_page",
                            class_name="nes-text is-error",
                            font_size=styles.Size.DEFAULT.value,                            
                            ),
                    rx.divider(
                            orientation="horizontal", 
                            variant="dashed", 
                            border_color=color.Color.ACCENT.value, 
                            ),
                ),
            ),
            rx.mobile_and_tablet(
                    rx.menu(
                        rx.menu_button("Menu"),
                        rx.menu_list(
                        rx.menu_item(
                            rx.link(
                            #Enlace a pagina formulario insercion datos
                            "Formulario Inserción", 
                            class_name="nes-text is-error", 
                            href="/Formulario", 
                            font_size=styles.Size.DEFAULT.value,
                            ),
                            bg="#ffab53",
                            ),
                        rx.menu_item(
                            rx.link(
                            #Enlace a pagina Tabla de datos de db remoto
                            "Tabla", 
                            href="/tabla", 
                            class_name="nes-text is-error",
                            font_size=styles.Size.DEFAULT.value,
                            ),
                            bg="#ffab53",
                            ),
                        rx.menu_item(
                            rx.link(
                            "Generador y Encriptador", 
                            href="/encrypt", 
                            class_name="nes-text is-error",
                            font_size=styles.Size.DEFAULT.value,
                            ),
                            bg="#ffab53",
                            ),
                        rx.menu_item(
                            rx.link(
                            "Volver", 
                            href="/Welcome_page", 
                            class_name="nes-text is-error",
                            font_size=styles.Size.DEFAULT.value,
                            ),
                            bg="#ffab53",
                            ),
                            bg="#ffab53",
                            width="95vw"
                        ),
                    ),
            ),

        bg="#ffab53",
        padding_x = "5px",
        padding_y = "10px",
        align_content="auto",
        z_index ="999",
        should_wrap_children=True,
        auto_flow="row", 
        max_width="95vw",
    )

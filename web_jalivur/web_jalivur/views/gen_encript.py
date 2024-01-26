import reflex as rx
from web_jalivur.components.passgen import NumberInputState
from web_jalivur.components.encrypt_pass import MsgInputState

def gen_enc_page():
    return rx.vstack(
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
                                    max_width="95vw",
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
                                max_width="95vw",
                            ),
                        
                        ),
                    rx.button(
                            "Limpiar", 
                            on_click=MsgInputState.limpiar(), 
                            class_name="nes-btn is-warning",
                            ),
                                    max_height="100vw",
    )
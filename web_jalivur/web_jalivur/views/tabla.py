
import reflex as rx
from web_jalivur.components.data_editor_own import editorstate
import web_jalivur.styles.themes as theme

def tabla_page():
    return rx.vstack(    
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
                        max_width="90vw",
                        position="relative",
                        padding="2%",
                        #left="",
                    ),
    )

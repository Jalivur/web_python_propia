import reflex as rx


def link_button(text:str, url:str ) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="arrow_forward",
                ),
                rx.vstack(
                    rx.text(text),
                    rx.text(text)
                )
            )
        ),
        href=url,
        is_external= True,
        width="100%"


    )


    return rx.link(
    rx.button(text, width="100%", margin_y="5px"),
    href=url,
    is_external= True,
    width="100%"
        
    )
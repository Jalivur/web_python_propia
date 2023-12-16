import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Jalivur",
            font_size="50px",
            color = "white"

        
        ),
        position = "sticky",
        bg="green",
        padding_x = "10px",
        padding_y = "10px",
        z_index ="999",
        border_radius="25%"
    )

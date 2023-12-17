import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "@Jalivur",
            font_size="50px",
            color = "#842424",
            as_="strong"
        

        
        ),
        position = "sticky",
        bg="#ffab53",
        padding_x = "10px",
        padding_y = "10px",
        z_index ="999"
    )

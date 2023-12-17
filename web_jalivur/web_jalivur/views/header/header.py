import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Alberto Estella", size="xl"),
        rx.text("@Jalivur"),
        rx.text("HOLA 👋 Mi Nombre Es Alberto Estella"),
        rx.text("""Soy Tecnico De Mantenimento En WV Narra, y en mis ratoslibres
                aprendo programacion con Brais Moure, alias MoureDev, 
                es muy buen profesor.""")
    )
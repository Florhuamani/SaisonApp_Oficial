import reflex as rx

def search_page()->rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Buscar categoría"),
            rx.input(placeholder="Buscar una categoría..."),
            rx.button("Buscar"),
            rx.button("Volver a la página principal", on_click="/home"),
            spacing="4",
            align="center",
        ),
        padding="4",
        center_content=True,
    )
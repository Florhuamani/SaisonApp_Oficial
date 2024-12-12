import reflex as rx

def categoria_page()-> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Categorías"),
            rx.text("Explora los mejores productos."),
            rx.button("Volver a la página principal",on_click="/home"),
            spacing="4",
            align="center",
        ),
        padding="4",
        center_content=True,
    )
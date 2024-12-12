import reflex as rx

def inspiration_page():
    return rx.container(
        rx.vstack(
            rx.heading("Inspiración"),
            rx.text("Ideas y sugerencias para tus compras de temporada."),
            rx.button("Volver a la Página Principal", on_click="/home"),
            spacing="4",
            align="center",
        ),
        padding="4",
        center_content=True,
    )